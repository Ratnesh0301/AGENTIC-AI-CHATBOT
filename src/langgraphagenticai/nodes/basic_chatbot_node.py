class BasicChatbotNode:
    """Node that handles basic chatbot functionality"""
    def __init__(self, model):
        self.model = model
    
    def __call__(self, state: GraphState):
        response = self.model.invoke(state["messages"])
        state["messages"].append(response)
        return state