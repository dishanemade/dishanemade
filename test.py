from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
load_dotenv(override=True)

"""chatbot with proper history"""
llm=ChatGroq(model="openai/gpt-oss-20b")

print("My first Chatbot")

history=[]

while True:

    prompt=input("user: ")
    history.append(HumanMessage(content=prompt))
    if prompt.lower()=="exit":
        break
    response=llm.invoke(prompt)
    history.append(AIMessage(content=response.content))
    print(response.content)

print(history)
