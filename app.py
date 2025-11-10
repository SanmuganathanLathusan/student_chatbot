import streamlit as st
import os
from dotenv import load_dotenv

# LangChain imports 
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

# Load OpenAI API key from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="📘 PDF Q&A Chatbot", layout="wide")
st.title("📘 Ask Your PDF - RAG Chatbot")

# Upload PDF
uploaded_file = st.file_uploader("📤 Upload your PDF", type="pdf")

if uploaded_file:
    # Save PDF temporarily
    os.makedirs("data", exist_ok=True)
    pdf_path = os.path.join("data", uploaded_file.name)
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("📖 Reading and indexing PDF..."):
        # Load PDF and split into chunks
        loader = PyPDFLoader(pdf_path)
        pages = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        docs = text_splitter.split_documents(pages)

        # Create embeddings and vector DB
        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        vector_db = FAISS.from_documents(docs, embeddings)
        retriever = vector_db.as_retriever(search_kwargs={"k": 3})

        # Initialize LLM
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=OPENAI_API_KEY)

        # Create RetrievalQA chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True
        )

        st.success("✅ PDF processed successfully!")

        # Ask questions
        query = st.text_input("💬 Ask a question from your PDF:")

        if query:
            with st.spinner("🤔 Thinking..."):
                answer = qa_chain.run(query)
                st.write("### 🧠 Answer:")
                st.write(answer)
