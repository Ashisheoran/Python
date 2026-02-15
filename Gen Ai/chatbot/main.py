import langchain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY1")

# prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", " You are a helpful assistant, Please response to the user queries"),
        ("user", "Question:{question}")
    ]
)

# steamlit framework

st.title('Langchain Using GeminiAi')
input_text = st.text_input("Search the topic u want")

# Gemini LLM
 
llm = ChatGoogleGenerativeAI(
    model= "gemini-1.5-flash",
    google_api_key = gemini_api_key
    )
output_parsers= StrOutputParser()

chain = prompt | llm | output_parsers

if input_text:
    st.write(chain.invoke({'question': input_text}))