from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv(override=True)

llm=ChatGroq(model="openai/gpt-oss-20b")

print("My first Chatbot")

while True:
    prompt=input("user: ")
    if prompt.lower()=="exit":
        break
    
    response=llm.invoke(prompt)
    print(response.content)
