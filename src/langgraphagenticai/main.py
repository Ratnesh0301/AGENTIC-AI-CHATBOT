import streamlit as st
from src.langgraphagenticai.ui.streamlit_ui.loadui import LoadStreamlitUI

def load_langgraph_agenticai_app():
    """
    Load the LangGraph Agentic AI Chatbot application
    """
    ui = LoadStreamlitUI()
    ui.load_streamlit_ui()

    user_message = st.chat_input("You: ")

if __name__ == "__main__":
    load_langgraph_agenticai_app()
    