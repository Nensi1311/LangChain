from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Load the LLM
llm = OpenAI(model_name='gpt-3.5-turbo', temperature=0.7)

# Create a prompt template
prompt = PromptTemplate(
    input_variables=['topic'],
    template="Suggest a catchy blog title about {topic}."
)

# Create an LLMChain
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain with a specific topic
topic = input('Enter a topic: ')
output = chain.run(topic)

print("Generated Blog Title: ",output)