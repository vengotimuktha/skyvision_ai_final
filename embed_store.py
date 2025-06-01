from dotenv import load_dotenv
load_dotenv()

import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS

# Load the text
with open("data/extracted/output_text.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
)
texts = text_splitter.split_text(raw_text)

# Set your API key from the .env file
openai_api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = openai_api_key

# Create embeddings
embedding_model = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(texts, embedding_model)

# Save locally
vectorstore.save_local("data/skyvision_faiss_index")

print("FAISS index created and saved.")
