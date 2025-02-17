from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic.invoke(model="")

result = model.invoke("what is the capital of india?")

print(result.content)