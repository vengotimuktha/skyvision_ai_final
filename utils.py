# utils.py

import os
import pandas as pd
from PyPDF2 import PdfReader
from typing import List
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.faiss import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA

# Load environment variables from .env
load_dotenv()

def extract_text_from_pdf(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text

def extract_text_from_csv(csv_path: str) -> str:
    df = pd.read_csv(csv_path)
    rows_as_text = df.astype(str).apply(lambda row: " | ".join(row.values), axis=1).tolist()
    return "\n".join(rows_as_text)

def create_faiss_index(text: str, index_path: str) -> None:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = text_splitter.split_text(text)

    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables (.env).")

    embedding_model = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vectorstore = FAISS.from_texts(chunks, embedding_model)
    vectorstore.save_local(index_path)

def answer_query(index_path: str, query: str) -> (str, List[str]):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables (.env).")

    embedding_model = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vectorstore = FAISS.load_local(index_path, embedding_model, allow_dangerous_deserialization=True)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    llm = ChatOpenAI(temperature=0.3, model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)

    result = qa_chain.invoke({"query": query})
    answer = result.get("result", "No answer found.")
    sources = [doc.page_content for doc in result.get("source_documents", [])]
    return answer, sources
