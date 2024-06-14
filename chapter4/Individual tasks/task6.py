#Task6 --> Implementing pydantic using custom schema and getting the response accordingly
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain.chains.openai_functions.extraction import create_extraction_chain_pydantic
from langchain_community.document_loaders import PyPDFLoader
from typing import Optional
from langchain_core.pydantic_v1 import BaseModel, Field

class Experience(BaseModel):
    start_date: Optional[str] = Field(default=None, description="Start date")
    end_date: Optional[str] = Field(default=None, description="End date")
    description: Optional[str] = Field(default=None, description="Descriptions of job")
class Study(Experience):
    degree: Optional[str] = Field(default=None, description="")
    university: Optional[str] = Field(default=None, description="The university from which the candidate graduated")
    country: Optional[str] = Field(default=None, description="The country where the candidate lives")
    grade: Optional[str] = Field(default=None, description="CGPA of candidate in university")
class WorkExperience(Experience):
    company: Optional[str] = Field(default=None, description="The place where the candidate worked previously")
    job_title: Optional[str] = Field(default=None, description="Name of last organisation")
class Resume(BaseModel):
    first_name: Optional[str] = Field(default=None, description="First name of the candidate")
    last_name: Optional[str] = Field(default=None, description="Last name of the candidate")
    linkedin_url: Optional[str] = Field(default=None, description="Link to linkedin of the employee")
    email_address: Optional[str] = Field(default=None, description="Email address of the employee")
    nationality: Optional[str] = Field(default=None, description="Nationality of the employee")
    skill: Optional[str] = Field(default=None, description="Skills of the employee")
    study: Optional[Study] = Field(default=None, description="Qualification of the employee")
    work_experience: Optional[WorkExperience] = Field(default=None, description="Work experience of the employee")
    hobby: Optional[str] = Field(default=None, description="Hobby of the employee")

load_dotenv()
llm = ChatOpenAI()
pdf_path = "resume.pdf"
pdf_loader = PyPDFLoader(pdf_path)
docs = pdf_loader.load_and_split()
prompt = ChatPromptTemplate.from_messages(
   [
        (
           ""
        ),
        ("human", "{docs}"),
    ]
)
chain = prompt | llm.with_structured_output(schema=Resume)
try:
    result = chain.invoke(docs)
    print("Result:")
    print(result)
except Exception as e:
    print(e)




#######-----------------------Below code is a rough work of Task 6 and kept for reference and understanding in future
# class BaseModel(Bs):
#     class Config:
#         arbitrary_types_allowed = True

# from typing import Optional
# from pydantic.v1 import BaseModel
# from dotenv import load_dotenv

# load_dotenv()

# class Experience(BaseModel):
#     start_date: Optional[str]
#     end_date: Optional[str]
#     description: Optional[str]
# class Study(Experience):
#     degree: Optional[str]
#     university: Optional[str]
#     country: Optional[str]
#     grade: Optional[str]
# class WorkExperience(Experience):
#     company: str
#     job_title: str
# class Resume(BaseModel):
#     first_name: str
#     last_name: str
#     linkedin_url: Optional[str]
#     email_address: Optional[str]
#     nationality: Optional[str]
#     skill: Optional[str]
#     study: Optional[Study]
#     work_experience: Optional[WorkExperience]
#     hobby: Optional[str]
#     # class Config: 
#     #     arbitrary_types_allowed = True


# from langchain.chains import create_extraction_chain_pydantic
# from langchain.chat_models import ChatOpenAI
# from langchain.document_loaders import PyPDFLoader

# pdf_file_path = "mohit.pdf"
# pdf_loader = PyPDFLoader(pdf_file_path)
# docs = pdf_loader.load_and_split()
# llm = ChatOpenAI(model_name="gpt-3.5-turbo-0613")
# chain = create_extraction_chain_pydantic(pydantic_schema=Resume, llm=llm) 
# print(chain.invoke(docs))


# # from typing import Optional
# # from pydantic import BaseModel
# # from dotenv import load_dotenv
# # import os

# # load_dotenv()

# # # Define the models
# # class Experience(BaseModel):
# #     start_date: Optional[str]
# #     end_date: Optional[str]
# #     description: Optional[str]

# # class Study(Experience):
# #     degree: Optional[str]
# #     university: Optional[str]
# #     country: Optional[str]
# #     grade: Optional[str]

# # class WorkExperience(Experience):
# #     company: str
# #     job_title: str

# # class Resume(BaseModel):
# #     first_name: str
# #     last_name: str
# #     linkedin_url: Optional[str]
# #     email_address: Optional[str]
# #     nationality: Optional[str]
# #     skill: Optional[str]
# #     study: Optional[Study]
# #     work_experience: Optional[WorkExperience]
# #     hobby: Optional[str]
# #     class Config: 
# #         arbitrary_types_allowed = True


# # # Import langchain components
# # from langchain.chains import create_extraction_chain_pydantic
# # from langchain.chat_models import ChatOpenAI
# # from langchain.document_loaders import PyPDFLoader

# # # Load PDF and extract documents
# # pdf_file_path = "mohit.pdf"
# # try:
# #     pdf_loader = PyPDFLoader(pdf_file_path)
# #     docs = pdf_loader.load_and_split()
# # except Exception as e:
# #     print(f"Error loading PDF: {e}")
# #     docs = None

# # # Check if documents are loaded
# # if docs:
# #     # Initialize the LLM
# #     try:
# #         llm = ChatOpenAI(model_name="gpt-3.5-turbo-0613")
# #     except Exception as e:
# #         print(f"Error initializing LLM: {e}")
# #         llm = None

# #     # Create and run the extraction chain
# #     if llm:
# #         try:
# #             chain = create_extraction_chain_pydantic(pydantic_schema=Resume, llm=llm)
# #             result = chain.run(docs)
# #             print(result)
# #         except Exception as e:
# #             print(f"Error running extraction chain: {e}")
# # else:
# #     print("No documents to process.")



# Importing Packages
# from schema import Resume
# from dotenv import load_dotenv
# from langchain_openai import ChatOpenAI
# from langchain.chains.openai_functions.extraction import create_extraction_chain_pydantic
# from langchain_community.document_loaders import PyPDFLoader
# from typing import Optional
# from pydantic.v1 import BaseModel, Field
# class Experience(BaseModel):
#     start_date: Optional[str]= Field(
#         default=None, description="Start date"
#     )
#     end_date: Optional[str]= Field(
#         default=None, description="End date"
#     )
#     description: Optional[str]= Field(
#         default=None, description="Descriptions of job"
#     )
# class Study(Experience):
#     degree: Optional[str]= Field(
#         default=None, description="Degree of the candidate"
#     )
#     university: Optional[str]= Field(
#         default=None, description="The university from which the candidate graduated"
#     )
#     country: Optional[str]= Field(
#         default=None, description="The country where the candidate lives"
#     )
#     grade: Optional[str]= Field(
#         default=None, description="CGPA of candidate in university"
#     )
# class WorkExperience(Experience):
#     company: str= Field(
#         default=None, description="The place where the candidate worked previously"
#     )
#     job_title: str= Field(
#         default=None, description="Name of last organisation"
#     )
# class Resume(BaseModel):
#     first_name: str= Field(
#         default=None, description="First name of the candidate"
#     )
#     last_name: str= Field(
#         default=None, description="Last name of the candidate"
#     )
#     linkedin_url: Optional[str]= Field(
#         default=None, description="Link to linkedin of the employee"
#     )
#     email_address: Optional[str]= Field(
#         default=None, description="Email address of the employee"
#     )
#     nationality: Optional[str]= Field(
#         default=None, description="Nationality of the employee"
#     )
#     skill: Optional[str]= Field(
#         default=None, description="Skills of the employee"
#     )
#     study: Optional[Study]= Field(
#         default=None, description="Qualification of the employee"
#     )
#     work_experience: Optional[WorkExperience]= Field(
#         default=None, description="Work experience of the employee"
#     )
#     hobby: Optional[str]= Field(
#         default=None, description="Hobby of the employee"
#     )
# # Loading Environment Variables

# load_dotenv()
# llm = ChatOpenAI().with_structured_output
# pdf_path = "resume.pdf"
# pdf_loader = PyPDFLoader(pdf_path)
# docs = pdf_loader.load_and_split()
# chain = create_extraction_chain_pydantic(pydantic_schema=Resume,llm=llm)
# print("Result using invoke()")
# print(str(chain.invoke(docs)['text']))
# print("\nResult using str(chain.run())")
# print(str(chain.run(docs)))


# chain = create_extraction_chain_pydantic(pydantic_schema=Resume, llm=llm)
# prompt = PromptTemplate.from_template(skills_prompt_template)
