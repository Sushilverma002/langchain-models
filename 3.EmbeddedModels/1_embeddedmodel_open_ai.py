from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding   = OpenAIEmbeddings(model = "text-embedding-3-large", dimensions=32)

result = embedding.embed_query("Delhi is the capital of india")
print(str(result))

# multiple embedding in single go
documents = [
    "Hi, my name is sushil",
    "hi , i am 20 yr old",
    "hi i live in delhi"
]

result2 = embedding.embed_documents(documents)
print(str(result2))