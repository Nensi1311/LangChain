from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content='Tell me aboutLangChain')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)