from langgraphagenticai.tools.search_tool import SearchTool
from langgraph.prebuilt import ToolNode
from langgraphagenticai.state.state import GraphState

class WebSearchNode:
    def __init__(self, model, tools):
        self.model = model
        self.model_with_tools = self.model.bind_tools(tools)

    def __call__(self, state: GraphState):
        web_search_results = self.model_with_tools.invoke(state['messages'])
        return {"web_search_results": web_search_results}

    def should_web_search(self, state: GraphState):
        last_message = state['messages'][-1]
        if last_message.tool_calls:
            return "web_search"
        return "end"