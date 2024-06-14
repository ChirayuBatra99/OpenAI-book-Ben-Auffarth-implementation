#Task-2 --> Implementing LangChain Expression Language (LCEL)
from langchain.prompts import PromptTemplate
from langchain_community.llms import OpenAI
from langchain.schema import StrOutputParser
# from langchain.chains import SimpleChain
llm = OpenAI()
prompt = PromptTemplate.from_template(
    "Summarize this text in 5 words: {text}?"
)
text = "What type of mammal lays the biggest eggs?"
chain =  prompt | llm | StrOutputParser()
summary = chain.invoke({"text": text})
print(summary)

