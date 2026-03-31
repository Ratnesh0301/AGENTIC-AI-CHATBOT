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

        if usecase == "basic_chatbot":
            for event in graph.stream({'messages':('user',user_message)}):
                print(event.values())
                for value in event.values():
                    print(value['message'])
                    with st.chat_message('user'):
                        st.write_message(user_message)
                    with st.chat_message('assistant'):
                        st.write_message(value['message'].content)