from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

text = "delhi is the capital of India"


documents = [
    "Hi, my name is sushil",
    "hi , i am 20 yr old",
    "hi i live in delhi"
]
vector = embedding.embed_documents(documents)

print(str(vector))