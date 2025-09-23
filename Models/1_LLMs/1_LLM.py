# OpenAI API Key
# from langchain_openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()

# llm = OpenAI(model="gpt-3.5-turbo-instruct")

# result = llm.invoke("What is the capital of India?")

# print(result)


# OpenRouter API Key
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

completion = client.chat.completions.create(
  model="openai/gpt-3.5-turbo-instruct",
  messages=[
    {
      "role": "user",
      "content": "What is the capital of India?"
    }
  ]
)
print(completion.choices[0].message.content)