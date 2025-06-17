# 🎙️ AI-Powered Podcast Generation Agent

This is a Streamlit-based application that transforms text (from a URL, PDF, or TXT file) into an engaging podcast script using a local Mistral LLM (via Ollama) and converts that script to realistic voice using Google Cloud Text-to-Speech.

---

## 📌 Features

- 🔍 Extracts text from **URLs**, **PDFs**, and **TXT** files
- 🤖 Uses **Mistral (via Ollama)** for:
  - Podcast script generation
  - Topic extraction
  - Q&A about content
- 🧠 Script includes intro, topic segments, interludes, and conclusion
- 🗣️ Converts scripts to **natural MP3 audio** via **Google Cloud TTS**
- 🔧 Voice and speaking rate selection
- 📦 Downloadable outputs: TXT script, MP3 audio, and SRT captions

---

## 🧱 Project Structure

```bash
.
├── streamlit_app.py          # Main app interface (Streamlit)
├── input_parser.py           # Input processing (URL, PDF, TXT)
├── ollama_script.py          # Podcast script generation
├── qa_mistral.py             # Q&A functionality using Mistral
├── text_to_voice.py          # Google TTS generation
├── requirements.txt          # Python dependencies
├── my-tts-key.json           # Google TTS credentials (not tracked)
├── google cloud shell.txt    # Shell logs (Google Cloud setup)
└── cloud-tts-intro.md        # Tutorial HTML dump (optional)
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-Powered-Podcast-Generation-Agent.git
cd AI-Powered-Podcast-Generation-Agent
```

### 2. Install dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## 🔐 Google Cloud TTS Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Enable the **Text-to-Speech API**
3. Create a **service account** and download the JSON key (e.g., `tts-codelab.json`)
4. Set the environment variable:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="tts-codelab.json"
```

---

## 🧠 Local Mistral LLM (via Ollama)

Install [Ollama](https://ollama.com/) and pull the `mistral` model:

```bash
ollama run mistral
```

Ensure it is available at:

```bash
http://localhost:11434
```

---

## ▶️ Run the App

Use Streamlit to launch the app:

```bash
streamlit run streamlit_app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🧪 Example Workflow

1. Select `URL`, `PDF`, or `TXT` input.
2. Upload or paste a link.
3. Preview extracted text.
4. Ask any question about the content.
5. Generate full podcast script.
6. Choose voice and speaking rate.
7. Download the `.txt`, `.srt`, and `.mp3` outputs.

---

## 🧰 Voice Options

The following voice names are available (via Google TTS):

- `en-US-Neural2-F` — US Female
- `en-US-Neural2-D` — US Male
- `en-GB-Neural2-C` — UK Female
- `en-GB-Neural2-B` — UK Male
- `en-AU-Neural2-F` — Australian Female
- `en-AU-Neural2-D` — Australian Male

You can extend this list with other [supported voices](https://cloud.google.com/text-to-speech/docs/voices).

---

## 📄 Sample Output Files

- ✅ `podcast_script.txt` — generated script
- ✅ `podcast_audio.mp3` — final audio file
- ✅ `subtitles.srt` — subtitle file (1 second per line approx.)

---

## 📦 Requirements

```
streamlit
boto3
google-cloud-texttospeech
newspaper3k
PyPDF2
pydub
```

---

## 📚 References

- [Ollama Docs](https://ollama.com/)
- [Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech/docs)
- [newspaper3k](https://newspaper.readthedocs.io/)
- [Streamlit](https://streamlit.io/)

---

## 🙋 Authors

- **Sayedali Mohseni** – [GitHub](https://github.com/Sayedalimohseni)
- **Amir Hossein Shahriari**

---

## 💡 Future Improvements

- Add multilingual support
- Deploy via Docker or HuggingFace Spaces
- Add memory for user sessions
- Allow regeneration of specific sections only
