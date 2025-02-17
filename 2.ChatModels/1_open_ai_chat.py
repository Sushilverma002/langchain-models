from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model =ChatOpenAI(model='gpt-4',temperature=0.5 , max_completion_tokens=10)
#temperature -> is a parameter that contorl the randomness of a language model output , it affects how creative or determinstic the response are.
# max_completion_token in which how much data you want . ex 10 , 20 , 30 etc or it will hlep you to control you costing .
result = model.invoke('what is the capital of India?')

print(result)