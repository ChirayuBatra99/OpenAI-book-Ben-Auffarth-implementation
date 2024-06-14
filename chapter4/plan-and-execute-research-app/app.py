import streamlit as st
from streamlit.external.langchain import StreamlitCallbackHandler
import wikipedia

from agentloading import load_agent
from memory import MEMORY

st.set_page_config(page_title="QnA", page_icon="Q n A")
st.header("Ask me")

strategy = st.radio(
    "Reasoning strategy",
    ("plan-and-solve", "zero-shot-react", ))
                  

tool_names = st.multiselect(
    'Which tools yoou want to use?',
    [
        "google-search", "ddg-search",  "arxiv",
        "wikipedia", "python_repl", "pal-math",
        "llm-math"
    ],
    ["ddg-search",  "wikipedia"])

if st.sidebar.button("Clear message history"):
    MEMORY.chat_memory.clear()

avatars = {"human": "user", "ai": "assistant"}
for msg in MEMORY.chat_memory.messages:
    st.chat_message(avatars[msg.type]).write(msg.content)

assert strategy is not None
agent_chain = load_agent(tool_names=tool_names, strategy=strategy)

assistant = st.chat_message("assistant")
if prompt := st.chat_input(placeholder="Ask me anything!"):
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())
        response = agent_chain.invoke(
            {"input": prompt}, {"callbacks": [st_callback]}

        )
        st.write(response["output"])