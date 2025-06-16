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

```text
podcast_langchain_agent/
├── app/
│   ├── streamlit_langchain_chatbot.py      # Streamlit chatbot UI
│   └── langchain_agent.py                  # LangChain agent setup using Ollama
│
├── tools/
│   ├── __init__.py                         # LangChain Tool() definitions
│   └── podcast_tool.py                     # Tool wrappers around your podcast functions
│
├── core/                                   # Original podcast generator (unchanged)
│   ├── input_parser.py                     # Extract text from URL / PDF / TXT
│   ├── ollama_script.py                    # Mistral-based podcast script generator
│   ├── qa_mistral.py                       # Q&A using Mistral
│   └── text to voice.py                              # Google Cloud TTS for MP3 generation
│
├── data/                                   # (Optional) uploaded files directory
├── .env                                    # (Optional) environment variable config
├── requirements.txt                        # Dependency list
└── README.md                               # This file

---

### 1. 🔧 Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com/) with Mistral 7B:
  ```bash
  ollama run mistral


  (Optional) Google Cloud Text-to-Speech:

Download a service account JSON key

Save it as text_to_voice-key.json

Export it: export GOOGLE_APPLICATION_CREDENTIALS="text_to_voice-key.json"



### 2. 📦 Install Dependencies
pip install -r requirements.txt


### 3. ▶️ Run the App

```bash
streamlit run app/streamlit_langchain_chatbot.py

Example Prompts
"Generate a podcast from https://www.bbc.com/news/technology-12345678"

"Create a podcast from /tmp/my_article.pdf"

"Make a podcast from the uploaded TXT file at /tmp/tmpxyz.txt"

## 📥 Outputs

- 📄 Script preview
- 💾 Downloadable `.txt` and `.srt` formats
- 🔊 Optional `.mp3` file via Google TTS

## 🤝 Contributing

Pull requests welcome.  
Bug reports, feedback, and feature suggestions are appreciated.

