from langchain.memory import ConversationBufferMemory
from langchain.prompts import MessagesPlaceholder


def init_memory():
    return ConversationBufferMemory(
        memory_key='chat_history',
        return_messages=True,
        output_key='answer'
    )


MEMORY = init_memory()
CHAT_HISTORY = MessagesPlaceholder(variable_name="chat_history")