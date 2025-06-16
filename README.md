# 🎙️ AI Podcast Generator Agent

An AI-powered agent that turns any URL, PDF, or TXT into an engaging podcast script — using [Mistral 7B](https://mistral.ai/news/introducing-mistral-7b/) via [Ollama](https://ollama.com/), orchestrated with [LangChain](https://www.langchain.com/), and deployed with [Streamlit](https://streamlit.io/).

---

## ✨ Features

- 💬 Chat-based interface (Streamlit)
- 🧠 LangChain agent selects tools based on your request
- 🌐 Extracts content from URLs, PDFs, or TXT files
- 🛠️ Generates podcast scripts using Mistral 7B (via Ollama)
- 🔊 Converts scripts to MP3 using Google Cloud Text-to-Speech
- 📎 Download podcast in `.txt`, `.srt`, or `.mp3` formats

---

## 🧱 Project Structure


podcast_langchain_agent/
├── app/
│ ├── streamlit_langchain_chatbot.py # Streamlit chatbot UI
│ └── langchain_agent.py # LangChain agent setup
│
├── tools/
│ ├── init.py # LangChain Tool() definitions
│ └── podcast_tool.py # Tool wrappers for podcast functions
│
├── core/ # Original podcast generator (unchanged)
│ ├── input_parser.py
│ ├── ollama_script.py
│ ├── qa_mistral.py
│ └── text_to_voice.py
│
├── data/ # (Optional) uploaded files
├── .env # (Optional) for API keys
├── requirements.txt
└── README.md


---

## 🚀 Getting Started

### 1. 🔧 Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com/) with Mistral:
  ```bash
  ollama run mistral
  (Optional) Google Cloud Text-to-Speech:

Download a service account JSON key

Save it as text_to_voice-key.json

Export it: export GOOGLE_APPLICATION_CREDENTIALS="my-text_to_voice-key.json"



2. 📦 Install Dependencies
pip install -r requirements.txt

3. ▶️ Run the App
streamlit run app/streamlit_langchain_chatbot.py

Example Prompts
"Generate a podcast from https://www.bbc.com/news/technology-12345678"

"Create a podcast from /tmp/my_article.pdf"

"Make a podcast from the uploaded TXT file at /tmp/tmpxyz.txt"


Contributing
Pull requests welcome.
Bug reports, feedback, and feature suggestions are appreciated.

---

Would you like me to generate and upload a `requirements.txt`, `.gitignore`, or `.zip` of the project next?
