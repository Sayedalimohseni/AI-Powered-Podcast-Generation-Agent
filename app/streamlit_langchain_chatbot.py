# streamlit_langchain_chatbot.py

import streamlit as st
from langchain_agent import agent
import tempfile

st.set_page_config(page_title="LangChain Podcast Agent 🤖🎙️")
st.title("💬 LangChain-Powered Podcast Generator")

if "history" not in st.session_state:
    st.session_state["history"] = []

user_prompt = st.chat_input("Ask me to generate a podcast from a URL, PDF, or TXT")

if user_prompt:
    st.chat_message("user").write(user_prompt)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = agent.run(user_prompt)
            st.write(result)
            st.session_state["history"].append(("user", user_prompt))
            st.session_state["history"].append(("assistant", result))

# --- Upload a file (optional)
st.subheader("📎 Upload File (PDF/TXT)")
uploaded_file = st.file_uploader("Upload your file")

if uploaded_file:
    suffix = "." + uploaded_file.name.split(".")[-1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    st.success(f"✅ File uploaded: {uploaded_file.name}")
    st.info(f"Now say: 'Generate a podcast from the uploaded {suffix.upper()} at path `{tmp_path}`'")
