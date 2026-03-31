from langgraph.graph import StateGraph, START, END
from langgraphagenticai.state.state import GraphState
from langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode

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

    def setup_graph(self, usecase):
        """Sets up the graph based on the usercase.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        
        return self.graphbuilder.compile()

        