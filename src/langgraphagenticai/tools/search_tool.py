from langchain_community.tools import TavilySearchResults

class SearchTool:
    def __init__(self):
        self.search_tool = TavilySearchResults(max_results=2)

    def get_search_tool(self):
        return self.search_tool