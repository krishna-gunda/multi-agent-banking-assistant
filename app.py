from flask import Flask, render_template, request

from dotenv import load_dotenv
import os

from langchain_chroma import Chroma

from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

load_dotenv()

os.environ["GROQ_API_KEY"]= os.getenv('GROQ_API_KEY')
print(os.getenv("GROQ_API_KEY"))
app = Flask(__name__)

embedding_model = HuggingFaceEmbeddings(
    model_name="intfloat/multilingual-e5-base"
)

llm = ChatGroq(
    model="llama-3.1-8b-instant",temperature=0
)

prompt = ChatPromptTemplate.from_template(
"""
You are a Back AI Assistant.

Answer only from the context.

<context>
{context}
</context>

Question:
{input}
"""
)

document_chain = create_stuff_documents_chain(
    llm,
    prompt
)

department_db = {

    "Account_Opening":
        "Account_Opening_KnowledgeBase.docx database",

    "Credit_Card":
        "Credit_Card_Department_KnowledgeBase.docx database",

    "CSD":
        "CSD_KnowledgeBase.docx database",

    "FraudDetection":
        "FraudDetection_KnowledgeBase.docx database",

    "Insurance":
        "Insurance_KnowledgeBase.docx database",

    "Loan":
        "Loans_KnowledgeBase.docx database",

    "Reception":
        "Reception_Department_KnowledgeBase.docx database"
}


@app.route("/", methods=["GET", "POST"])
def home():

    answer = ""

    if request.method == "POST":

        department = request.form["department"]
        question = request.form["question"]

        vector_db = Chroma(
            persist_directory=
            "./db/" + department_db[department],

            embedding_function=
            embedding_model
        )

        docs = vector_db.similarity_search(
            question,
            k=5
        )

        result = document_chain.invoke(
            {
                "input": question,
                "context": docs
            }
        )

        answer = result

    return render_template(
        "index.html",
        answer=answer
    )


if __name__ == "__main__":
    app.run(debug=False)