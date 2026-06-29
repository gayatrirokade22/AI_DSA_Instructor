import streamlit as st
from rag import get_answer

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="AI DSA Instructor",
    page_icon="📘",
    layout="centered"
)

# -----------------------------
# SESSION STATE
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# CSS
# -----------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

header{
    visibility:hidden;
}

.stApp{
    background:#F8FAFC;
}

.block-container{
    max-width:850px;
    padding-top:2rem;
}

.title{
    text-align:center;
    font-size:42px;
    font-weight:700;
    color:#1F2937;
    margin-bottom:8px;
}

.subtitle{
    text-align:center;
    color:#6B7280;
    font-size:17px;
    margin-bottom:35px;
}

.stTextInput input{
    height:60px !important;
    border-radius:16px !important;
    border:2px solid #D6E4F5 !important;
    font-size:18px !important;
    padding-left:18px !important;
    background:white !important;
}

.stButton>button{
    width:100%;
    height:44px;
    border-radius:12px;
    border:1px solid #D6E4F5;
    background:white;
    font-weight:500;
}

.stButton>button:hover{
    border-color:#4F7DF3;
    background:#EEF4FF;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------

if len(st.session_state.messages) == 0:

    st.markdown("""
    <div class="title">
    AI DSA Instructor
    </div>

    <div class="subtitle">
    Ask questions from your DSA notes
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# SEARCH BAR
# -----------------------------

question = st.text_input(
    "",
    placeholder="Ask a question...",
    label_visibility="collapsed"
)

# -----------------------------
# SUGGESTED QUESTIONS
# -----------------------------

if len(st.session_state.messages) == 0:

    st.markdown("### Suggested Questions")

    suggestions = [
        "What is Linked List?",
        "Explain AVL Tree",
        "What is Queue?",
        "Difference between BFS and DFS"
    ]

    for q in suggestions:

        if st.button(q):

            question = q

# -----------------------------
# ASK QUESTION
# -----------------------------

if question:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":question
        }
    )

    with st.spinner("Searching your notes..."):

        answer = get_answer(question)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )

    st.rerun()

# -----------------------------
# CHAT
# -----------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# -----------------------------
# CHAT INPUT
# -----------------------------

prompt = st.chat_input("Ask another question...")

if prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.spinner("Searching your notes..."):

        answer = get_answer(prompt)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )

    st.rerun()