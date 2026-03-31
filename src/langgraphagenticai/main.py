import streamlit as st
from langgraphagenticai.ui.streamlit_ui.loadui import LoadStreamlitUI
from langgraphagenticai.graph.graph_builder import GraphBuilder
from langgraphagenticai.llms.groq_llm import GroqLLM
from langgraphagenticai.ui.streamlit_ui.display_results import DisplayResultsStreamlit


def load_langgraph_agenticai_app():
    """
    Load the LangGraph Agentic AI Chatbot application
    """
    ui = LoadStreamlitUI()
    ui.load_streamlit_ui()

    user_message = st.chat_input("You: ")

    if user_message:
        try:
            #Configure the LLMs
            obj_llm_config = GroqLLM(user_controls_input=user_message)
            llm = obj_llm_config.get_groq_llm()

            if not llm:
                st.error("LLM configuration failed. Please check your API key and model.")
                return

            #Initialize and setup graph based on usecase
            usecase = user_input.get('selected_usecase')

            if not usecase:
                st.error("Please select a usecase.")
                return

            #Graph Builder
            graph_builder = GraphBuilder(model=llm)
            try:
                graph_builder.setup_graph(usecase)
                DisplayResultsStreamlit(usecase,graph,user_message).display_results_on_ui()
            except Exception as e:
                st.error(f"Error setting up graph: {str(e)}")
                return
        except Exception as e:
            st.error(f"Error: {str(e)}")
            return

if __name__ == "__main__":
    load_langgraph_agenticai_app()
    