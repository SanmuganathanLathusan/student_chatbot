# 📚 University Student RAG Chatbot

A smart and interactive chatbot designed for university students to **upload PDF lecture notes** and ask **subject-related questions**.  
The chatbot provides **accurate, context-aware answers** using **RAG (Retrieval Augmented Generation)** combined with **LLMs**.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 📄 **PDF Upload** | Upload your lecture notes, slides, or subject PDFs |
| 🔍 **RAG Search** | Bot retrieves the **exact relevant content** from your notes |
| 🤖 **AI Answer Generation** | Uses an LLM to provide **clear, structured answers** |
| 💾 **Persistent Vector Storage** | Your uploaded notes are saved — no need to re-upload |
| 💬 **Conversation Memory** | The chatbot remembers previous chat context |
| 🔐 **User Authentication** | Only registered students can access the chatbot |

---

## 🧱 Tech Stack

| Component | Technology |
|----------|------------|
| Frontend UI | **Streamlit** |
| Document Loader | **PyPDF / LangChain** |
| Text Embeddings | **Sentence Transformer (MiniLM)** |
| Vector Database | **FAISS** |
| LLM Model | **OpenAI / (Optional) Groq LLaMA, Mixtral** |
| Backend Development | **Python** |



---
## 📂 Project Structure
student_chatbot/
│── app.py 
│── users.json 
│── vectorstore/ 
│── requirements.txt 
│── README.md 
----


---

## 🧑‍🎓 How It Works

1. Student logs into the chatbot
2. Uploads PDF lecture notes (only once)
3. The system converts text → embeddings → stores in FAISS
4. Student asks questions in natural language
5. Chatbot retrieves matching chunks + uses LLM to generate final answer

---





