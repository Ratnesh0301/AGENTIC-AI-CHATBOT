import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input
        self.groq_api_key = user_controls_input["groq_api_key"]
        self.groq_model = user_controls_input["groq_model"]

        if not self.user_controls_input["groq_api_key"]:
            st.warning("Please enter your Groq API Key")
        else:
            st.success("Groq API Key validated")

        if not self.user_controls_input["groq_model"]:
            st.warning("Please select your Groq Model")
        else:
            st.success("Groq Model validated")

    def get_groq_llm(self):
        return ChatGroq(
            api_key=self.groq_api_key,
            model=self.groq_model
        )
        