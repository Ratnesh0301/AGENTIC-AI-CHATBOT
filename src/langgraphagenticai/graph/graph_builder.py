from langgraph.graph import StateGraph, START, END
from langgraphagenticai.state.state import GraphState
from langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode

class GraphBuilder:
    def __init__(self, model):
        self.model = model
        self.graphbuilder = GraphState(state)

    def basic_chatbot_build_graph(self):
        """Builds the basic chatbot graph. 
        This method initializes a chatbot node using the 'BasicChatbotNode' class
        and integrates it into the graph. the chatbot node is set as both the entry and exit point of the graph."""

        self.graphbuilder.add_node('chatbot',"")
        self.graphbuilder.add_edge(START, 'chatbot')
        self.graphbuilder.add_edge('chatbot', END)
        self.basic_chatbot_node = BasicChatbotNode(self.model)
        self.graphbuilder.add_edge('chatbot', self.basic_chatbot_node.__call__)

    def setup_graph(self, usecase):
        """Sets up the graph based on the usercase.
        """
        if usecase == "basic_chatbot":
            self.basic_chatbot_build_graph()
        
        return self.graphbuilder.compile()

        