import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json

class DisplayResultsStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_results_on_ui(self):
        """
        Display the results of the graph execution on the UI
        """
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message

        if usecase == "Basic Chatbot":
            for event in graph.stream({'messages':('user',user_message)}):
                print(event.values())
                for value in event.values():
                    print(value['messages'])
                    with st.chat_message('user'):
                        st.write(user_message)
                    with st.chat_message('assistant'):
                        st.write(value['messages'].content)

        elif usecase == "AI News":
            frequency = self.user_message
            with st.spinner("Fetching and summarizing the news..."):
                result = graph.invoke({'messages':frequency})
                try:
                    #Read the markdown file
                    AI_NEWS_PATH = f"./AI_NEWS/{frequency.lower()}.md"
                    with open(AI_NEWS_PATH,'r') as f:
                        markdown_content = f.read()
                    st.markdown(markdown_content,unsafe_allow_html=True)
                except FileNotFoundError:
                    st.error("AI News file not found. Please run the graph first.")
                except Exception as e:
                    st.error(f"Error reading AI News file: {str(e)}")


        elif usecase == "Chatbot with Web":
            for event in graph.stream({'messages':('user',user_message)}):
                print(event.values())
                for value in event.values():
                    print(value['messages'])
                    with st.chat_message('user'):
                        st.write(user_message)
                    with st.chat_message('assistant'):
                        st.write(value['messages'].content)