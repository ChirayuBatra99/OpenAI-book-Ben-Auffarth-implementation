#Task5 --> Tracking token usage in OpenAI
from langchain import OpenAI, PromptTemplate
from langchain.callbacks import get_openai_callback
llm_chain = PromptTemplate.from_template("Tell me a joke about {topic}!") | OpenAI()
with get_openai_callback() as cb:
    response = llm_chain.invoke(dict(topic="light bulbs"))
    print(response)
    print(f"Total Tokens: {cb.total_tokens}")
    print(f"Prompt Tokens: {cb.prompt_tokens}")
    print(f"Completion Tokens: {cb.completion_tokens}")
    print(f"Total Cost (USD): ${cb.total_cost}")