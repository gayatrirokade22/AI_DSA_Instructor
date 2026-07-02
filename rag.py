from dotenv import load_dotenv

from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI
)

from langchain_community.vectorstores import FAISS

# Load API Key
load_dotenv()

# Embedding Model
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview"
)

# LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3
)

# Load FAISS
vector_store = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)


def get_answer(query):

    docs = vector_store.similarity_search(query, k=10)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are a helpful DSA instructor.

Answer the user's question using only the context below.

If the answer is not available in the context, reply:
"I couldn't find the answer in the provided notes."

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    return response.content