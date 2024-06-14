#This code is for personal reference in future



import streamlit as st
from langchain.agents import (
    AgentExecutor, AgentType, initialize_agent, load_tools
)
# from langchain.callbacks.streamlit import StreamlitCallbackHandler
from dotenv import load_dotenv
import os
load_dotenv()
import wikipedia
from langchain.agents import load_tools

os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

from langchain_community.chat_models import ChatOpenAI
from langchain.agents import load_tools
def load_agent() -> AgentExecutor:
    llm = ChatOpenAI(temperature=0, streaming=True)
    # DuckDuckGoSearchRun, wolfram alpha, arxiv search, wikipedia # TODO: try wolfram-alpha!
    # tools = load_tools(tool_names=["ddg-search", "wolfram-alpha", "arxiv", "wikipedia"],llm=llm )
    tools = load_tools( ["ddg-search", "wolfram-alpha", "arxiv", "wikipedia"] )
    return initialize_agent(tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)

# chain = load_agent()
# st_callback = StreamlitCallbackHandler(st.container())
# if prompt := st.chat_input():
#     st.chat_message("user").write(prompt)
#     with st.chat_message("assistant"):
#         st_callback = StreamlitCallbackHandler(st.container())
#         response = chain.run(prompt, callbacks=[st_callback])
#         st.write(response)