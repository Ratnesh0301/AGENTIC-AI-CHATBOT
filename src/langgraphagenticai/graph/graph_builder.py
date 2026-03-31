from langgraph.graph import StateGraph, START, END
from langgraphagenticai.state.state import GraphState
from langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from langgraphagenticai.tools.search_tool import SearchTool
from langgraphagenticai.nodes.web_search_node import WebSearchNode
from langgraphagenticai.nodes.ai_news_node import AINewsNode

class GraphBuilder:
    def __init__(self, model):
        self.model = model
        self.graphbuilder = StateGraph(GraphState)

    def basic_chatbot_build_graph(self):
        """Builds the basic chatbot graph. 
        This method initializes a chatbot node using the 'BasicChatbotNode' class
        and integrates it into the graph. the chatbot node is set as both the entry and exit point of the graph."""

        self.basic_chatbot_node = BasicChatbotNode(self.model)
        self.graphbuilder.add_node('chatbot', self.basic_chatbot_node)
        self.graphbuilder.add_edge(START, 'chatbot')
        self.graphbuilder.add_edge('chatbot', END)

    def ai_news_builder_graph(self):
        """
        Builds the AI news graph.
        """
        self.ai_news_node = AINewsNode(self.model)
        self.graphbuilder.add_node("fetch_news",self.ai_news_node.fetch_news)
        self.graphbuilder.add_node("summarize_news",self.ai_news_node.summarize_news)
        self.graphbuilder.add_node("save_results",self.ai_news_node.save_results)

        self.graphbuilder.set_entry_point("fetch_news")
        self.graphbuilder.add_edge("fetch_news","summarize_news")
        self.graphbuilder.add_edge("summarize_news","save_results")
        self.graphbuilder.add_edge("save_results",END)
        

    def setup_graph(self, usecase):
        """Sets up the graph based on the usercase.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()

        elif usecase == "Chatbot with Web":
            self.chatbot_with_web_build_graph()

        elif usecase == "AI News":
            self.ai_news_builder_graph()
        
        return self.graphbuilder.compile()

    def chatbot_with_web_build_graph(self):
        """
        Builds an advanced chatbot graph with tool integration.This methods create a graph hat includes both chatbot node and web search tool node.
        """
        from langgraph.prebuilt import ToolNode, tools_condition

        ##Define the tool and tool nodes
        search_tool = SearchTool().get_search_tool()
        tools = [search_tool]
        tool_node = ToolNode(tools=tools)

        ##Define the chatbot node
        llm_with_tools = self.model.bind_tools(tools)
        def chatbot_node_func(state: GraphState):
            return {"messages": [llm_with_tools.invoke(state["messages"])]}

        ##Define the graph
        self.graphbuilder.add_node('chatbot', chatbot_node_func)
        self.graphbuilder.add_node('web_search', tool_node)

        ##Define the edges
        self.graphbuilder.add_edge(START, 'chatbot')
        self.graphbuilder.add_conditional_edges(
            'chatbot',
            tools_condition,
            {"tools": "web_search", "__end__": END}
        )
        self.graphbuilder.add_edge('web_search', 'chatbot')
