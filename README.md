# 🏦 Multi-Department RAG Banking Assistant

An enterprise-grade Retrieval-Augmented Generation (RAG) application that enables department-specific question answering using banking knowledge bases. The system leverages LangChain, ChromaDB, Hugging Face Embeddings, Groq LLaMA models, and Flask to provide accurate, context-aware responses grounded in internal documents.

---

## 📌 Overview

Banking organizations maintain large volumes of documentation across multiple departments. Finding accurate information manually can be slow and inefficient.

This project solves that challenge by creating a department-aware AI assistant that:

- Retrieves information from department-specific knowledge bases
- Uses semantic search instead of keyword matching
- Generates answers only from retrieved context
- Reduces hallucinations through Retrieval-Augmented Generation (RAG)
- Maintains separate vector databases for different departments

---

## 🚀 Features

### Department-Specific Knowledge Bases

The system supports:

- 🏦 Account Opening
- 💳 Credit Card
- 🎧 Customer Service
- 🛡️ Fraud Detection
- 📋 Insurance
- 💰 Loans
- 🏢 Reception

Each department has its own ChromaDB vector store for accurate and isolated retrieval.

### Retrieval-Augmented Generation (RAG)

- Document Processing
- Text Chunking
- Embedding Generation
- Vector Search
- Top-5 Context Retrieval
- LLM-Based Response Generation

### Semantic Search

- Hugging Face multilingual embeddings
- ChromaDB vector storage
- Similarity-based retrieval
- Context-aware answering

### Modern AI Stack

- Groq LLaMA Models
- LangChain
- ChromaDB
- Hugging Face Embeddings
- Flask

---

## 🏗️ System Architecture

```text
User Question
      │
      ▼
Department Selection
      │
      ▼
Load Department Vector Database
      │
      ▼
Top-5 Similarity Search
      │
      ▼
Retrieved Context
      │
      ▼
Groq LLaMA Model
      │
      ▼
Generated Response
```

---

## 📂 Project Structure

```text
Multi-Department-RAG-Banking-Assistant/
│
├── data/
│   ├── Account_Opening_Department_Knowledge_Base.docx
│   ├── Credit_Card_Department_Knowledge_Base.docx
│   ├── CustomerServiceDepartment_Knowledge_Base.docx
│   ├── FraudDetection_KnowledgeBase.docx
│   ├── Insurance_Knowledge_Base.docx
│   ├── Loans_Knowledge_Base.docx
│   └── Reception_Department_Knowledge_Base.docx
│
├── DB/
│   ├── Account_Opening/
│   ├── Credit_Card/
│   ├── Customer_Service/
│   ├── Fraud_Detection/
│   ├── Insurance/
│   ├── Loans/
│   └── Reception/
│
├── templates/
│   └── index.html
│
├── app.py
├── embeddings.py
├── requirements.txt
├── .env
└── README.md
```

---

## 🛠️ Technology Stack

| Category | Technology |
|-----------|------------|
| Backend | Flask |
| LLM | Groq LLaMA 3 |
| Framework | LangChain |
| Vector Database | ChromaDB |
| Embeddings | multilingual-e5-base |
| Environment Variables | python-dotenv |
| Frontend | HTML, CSS, JavaScript |

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Multi-Department-RAG-Banking-Assistant.git

cd Multi-Department-RAG-Banking-Assistant
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
HF_TOKEN=your_huggingface_token
```

---

## 📚 Generate Embeddings

Run the embedding pipeline:

```bash
python embeddings.py
```

This will:

1. Load department knowledge base documents
2. Split documents into chunks
3. Generate embeddings
4. Store vectors in ChromaDB

---

## ▶️ Run the Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 🔄 Workflow

### Step 1

User selects a department.

### Step 2

User enters a question.

### Step 3

The system loads the corresponding ChromaDB vector database.

### Step 4

Top 5 relevant chunks are retrieved using similarity search.

### Step 5

Retrieved context is sent to the Groq LLaMA model.

### Step 6

The model generates a context-aware answer.

### Step 7

The answer is displayed in the web application.

---

## 💡 Example Questions

### Account Opening

- What documents are required to open a savings account?
- What is the minimum balance requirement?

### Loans

- What documents are needed for a home loan?
- What are the loan eligibility criteria?

### Fraud Detection

- How are suspicious transactions investigated?
- What steps should be taken when fraud is detected?

### Credit Card

- What are the eligibility requirements for a credit card?
- How can a customer increase their credit limit?

---

## 🎯 Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Semantic Search
- Vector Databases
- Prompt Engineering
- LangChain
- ChromaDB
- Flask Development
- Knowledge Base Systems
- AI Application Development

---

## 🔮 Future Enhancements

- Multi-Agent Routing
- Automatic Department Detection
- Conversation Memory
- Hybrid Search
- Source Citation Display
- User Authentication
- Role-Based Access Control
- Streaming Responses
- PostgreSQL Integration

---

## 📸 Screenshots

Add screenshots here:

```text
screenshots/
├── homepage.png
├── department_selection.png
├── chatbot_interface.png
└── response_example.png
```

---

## 👨‍💻 Author

### G. Krishna

AI/ML Engineer | Data Scientist | Generative AI Enthusiast

### Technical Skills

- Python
- Machine Learning
- Deep Learning
- Natural Language Processing
- LangChain
- ChromaDB
- Groq
- Flask
- SQL
- TensorFlow
- PyTorch

### Connect With Me

GitHub:
[https://github.com/gundakrishna338](https://github.com/krishna-gunda)

LinkedIn:
www.linkedin.com/in/g-krishna630534

---

## ⭐ Support

If you found this project useful:

- Star this repository ⭐
- Fork this repository 🍴
- Share feedback 💡

---

## 📄 License

This project is licensed under the MIT License.
