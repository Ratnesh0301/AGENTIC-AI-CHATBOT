from langgraph.channels import topic
from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate

class AINewsNode:
    def __init__(self,model):
        """
            Initializes the AINewsNode with the given model.
        """
        self.llm = llm
        self.tavily = TavilyClient()
        #This is used to capture various stepsin this file so that we can use it in the graph builder
        self.state = {}

        def fetch_news(self, state:dict) -> dict:
            """
            Fetches the latest news using the Tavily API.
            
            Args:
                state (dict): The current state of the graph.
            
            Returns:
                dict: The updated state with 'new_data' key containing the fetched news.
            """

            frequency = state['messages'][0].content.lower()
            self.state['frequency'] = frequency
            time_range_map = {'daily':'d','weekly':'w','monthly':'m','yearly':'y'}
            days_map = {'daily':1, 'weekly':7, 'monthly':30, 'yearly':366}
            
            response = self.tavily.search(
                query="Top Artificial Intelligence (AI) technology news India and globally",
                topic='news',
                time_range=time_range_map[frequency],
                max_results=15,
                days=days_map[frequency],
                # include_domains=['techcrunch.com','venturebeat.com/ai'] #uncomment and add domains if needed
            )

            state['news_data'] = response.get('results',[])
            self.state['news_data'] = state['news_data']
            return state

        def summarize_news(self,state:dict) -> dict:
            """
            Summarizes the fetched news using the LLM.
            
            Args:
                state (dict): The current state of the graph.
            
            Returns:
                dict: The updated state with 'summary' key containing the summarized news.
            """
            news_items = self.state["news_data"]

            prompt_template = ChatPromptTemplate.from_messages(
                [
                    ('system',"""
                    You are an expert AI news analyst.
                    Your task is to summarize the following AI news articles.
                    Focus on key developments, breakthroughs, and significant announcements.
                    Keep the summary concise but comprehensive.
                    Follow the below format:
                    - date in **YYYY-MM-DD** format in IST timezone
                    - concise sentencs summary from latest news
                    - sort news by date wise (latest first)
                    - Source URL as link

                    ### [DATE]
                    - [TITLE](URL)
                    - [TITLE](URL)
                    - [TITLE](URL)
                    """
                    ), 
                    ('user',"""
                    Here are the AI news articles:\n\n
                    {articles}
                        """)
                ]
            )

            articles_str = "\n\n".join([
                f"Content: {item.get('content','')}\n   "
                f"URL: {item.get('url','')}\n"
                f"Title: {item.get('title','')}\n"
                f"Published At: {item.get('published_at','')}\n"
                f"Source: {item.get('source','')}\n"
                for item in news_items
            ])

            response = self.llm.invoke(prompt_template.format(articles=articles_str ))
            state['summary'] = response.content
            self.state['summary'] = state['summary'] 
            return self.state

        def save_results(self,state):
            """
            Saves the summarized news to a file.
            
            Args:
                state (dict): The current state of the graph.
            
            Returns:
                dict: The updated state with 'summary' key containing the summarized news.
            """
            frequency = self.state['frequency']
            summary = self.state['summary']
            filename = f"./AINews/ai_news_{frequency}.md"
            print(filename)
            with open(filename,'w') as f:
                f.write(f"{frequency.capitalize()} AI News Summary\n\n")
                f.write(summary)
            self.state['filename'] = filename
            return self.state




            
            