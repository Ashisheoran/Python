from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes
import uvicorn 
import os
from dotenv import load_dotenv

load_dotenv()


os.environ['GOOGLE_API_KEY'] = os.getenv('GEMINI_API_KEY1')
# os.environ["gemini_api_key2"] = os.getenv('GEMINI_API_KEY2')


app = FastAPI(
    title = "Langchain Server",
    version="1.0",
    description="A simple API Server"
) 

# add_routes(
#     app,
#     ChatGoogleGenerativeAI(model='gemini-1.5-flash'),
#     path = "/geminiAI"
# )                           

model1 = ChatGoogleGenerativeAI(model='gemini-1.5-flash')
model2 = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} in 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me an poem about {topic} in 100 words")

add_routes(
    app,
    prompt1 | model1,
    path = "/essay"
)
    
add_routes(
    app,
    prompt2 | model2,
    path = "/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000 )
    