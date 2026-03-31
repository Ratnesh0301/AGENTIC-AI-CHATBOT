import streamlit as st
import os
from langgraphagenticai.ui.uiconfig import UIConfig

class LoadStreamlitUI:
    def __init__(self):
        self.config = UIConfig()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(
            page_title=self.config.get_page_title(),
            page_icon="🤖",
            layout="wide",
        )
        st.header(self.config.get_page_title(), divider="blue")
        st.session_state.IsFetchButtonClicked = False
        st.session_state.time_frame = ""

        with st.sidebar:
            #Get options from sidebar
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()
            
            #LLM Selection
            self.user_controls["llm"] = st.selectbox(
                "Select LLM",
                options=llm_options,
                index=0,
                help="Choose the Large Language Model to use"
            )

            if self.user_controls["llm"] == "Groq":
                groq_model_options = self.config.get_groq_model_options()
                self.user_controls["groq_model"] = st.selectbox(
                    "Groq Model",
                    options=groq_model_options,
                    index=0,
                    help="Choose the Groq Model to use"
                )
                self.user_controls["groq_api_key"] = st.session_state['GROQ_API_KEY'] = st.text_input(
                    "Groq API Key",
                    type="password",
                    help="Enter your Groq API Key"
                )

                #Validate GROQ API KEY
                if not self.user_controls["groq_api_key"]:
                    st.warning("Please enter your Groq API Key")
                else:
                    os.environ["GROQ_API_KEY"] = self.user_controls["groq_api_key"]
                    st.success("Groq API Key validated")

                #Usecase Selection
                self.user_controls["usecase"] = st.selectbox(
                    "Select Usecase",
                    options=usecase_options,
                    index=0,
                    help="Choose the Usecase to use"
                )

                #Validate Usecase
                if not self.user_controls["usecase"]:
                    st.warning("Please select a Usecase")
                else:
                    st.success("Usecase selected")

                if self.user_controls['usecase'] == "Chatbot with Web" or self.user_controls['usecase'] == "AI News":
                    os.environ["TAVILY_API_KEY"] = self.user_controls['TAVILY_API_KEY'] = st.session_state['TAVILY_API_KEY'] = st.text_input(
                        "Tavily API Key",
                        type="password",
                        help="Enter your Tavily API Key"
                    )

                    #Validate TAVILY API KEY
                    if not self.user_controls['TAVILY_API_KEY']:
                        st.warning("Please enter your Tavily API Key")
                    else:
                        st.success("Tavily API Key validated")

                if self.user_controls['usecase'] == "AI News":
                    st.subheader("AI News Explorer")
                    with st.sidebar:
                        st.subheader("AI News Configuration")
                        time_frame = st.selectbox(
                            "Select Time Frame",
                            ["Daily", "Monthly", "Weekly"],
                            index=0,
                            help="Choose the Time Frame for AI News"
                        )
                    if st.button("Fetch Latest AI News", use_container_width=True):
                        st.session_state.IsFetchButtonClicked = True
                        st.session_state.timeframe = time_frame
    