import logging
import streamlit as st
from streamlit.external.langchain import StreamlitCallbackHandler
from retriever import configure_retrieval_chain
from load import MEMORY, DocumentLoader

logging.basicConfig(encoding="utf-8", level=logging.INFO)
LOGGER = logging.getLogger()

st.set_page_config(page_title="Document chat", page_icon="*")
st.title("Document Chat")

uploaded_files = st.sidebar.file_uploader(
    label="Upload files",
    type=list(DocumentLoader.supported_extensions.keys()),
    accept_multiple_files=True
)
if not uploaded_files:
    st.info("Please upload something")
    st.stop()

use_compression = st.checkbox("compression", value=False)
use_flare = st.checkbox("flare", value=False)
use_moderation = st.checkbox("moderation", value=False)

CONV_CHAIN = configure_retrieval_chain(
    uploaded_files,
    use_compression=use_compression,
    use_flare=use_flare,
    use_moderation=use_moderation
)

if st.sidebar.button("Clear history"):
    MEMORY.chat_memory.clear()

avatars = {"human": "user", "ai": "assistant"}

if len(MEMORY.chat_memory.messages) == 0:
    st.chat_message("assistant").markdown("Ask here")

for msg in MEMORY.chat_memory.messages:
    st.chat_message(avatars[msg.type]).write(msg.content)

assistant = st.chat_message("assistant")
if user_query := st.chat_input(placeholder="Give 3 keywords"):
    st.chat_message("user").write(user_query)
    container = st.empty()
    stream_handler = StreamlitCallbackHandler(container)
    with st.chat_message("assistant"):
        if use_flare:
            params = {
                "user_input": user_query,
            }
        else:
            params = {
                "question": user_query,
                "chat_history": MEMORY.chat_memory.messages,
            }
        response = CONV_CHAIN.run(params, callbacks=[stream_handler])
        if response:
            container.markdown(response)