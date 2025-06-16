# streamlit_app.py
import streamlit as st
from input_parser import extract_text_from_url, extract_text_from_pdf, extract_text_from_txt
from ollama_script import generate_podcast_script_iterative
from qa_mistral import ask_mistral_question
from tts import text_to_speech
import tempfile

import time
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "my-tts-key.json"

st.set_page_config(page_title="AI Podcast Generator", layout="centered")
st.title("🎙️ AI-Powered Podcast Agent")

# --- Upload / URL input
st.subheader("📥 Upload a file or enter a URL")
input_type = st.radio("Choose input type:", ["URL", "PDF", "TXT"])

uploaded_file = None
url_input = None
text_data = ""

if input_type == "URL":
    url_input = st.text_input("Paste a URL")
    if st.button("Extract Text from URL") and url_input:
        with st.spinner("Extracting text from URL..."):
            text_data = extract_text_from_url(url_input)

elif input_type == "PDF":
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name
        with st.spinner("Extracting text from PDF..."):
            text_data = extract_text_from_pdf(tmp_path)

elif input_type == "TXT":
    uploaded_file = st.file_uploader("Upload TXT", type=["txt"])
    if uploaded_file:
        with st.spinner("Extracting text from TXT..."):
            text_data = uploaded_file.read().decode("utf-8")

# --- Display extracted text
if text_data:
    st.subheader("📝 Extracted Text")
    st.text_area("Content", text_data[:1000], height=200)
    st.subheader("❓ Q&A on Extracted Content")
    user_question = st.text_input("Ask a question about the extracted content:")

    # Only answer when the button is pressed
    if st.button("Get Answer") and user_question:
        with st.spinner("Thinking..."):
            answer = ask_mistral_question(text_data, user_question)
        st.text_area("Answer", answer, height=150)


# --- Voice Selection
st.subheader("🎛️ Voice Selection")
voice_options = {
    "US - Female (Neural2-F)": "en-US-Neural2-F",
    "US - Male (Neural2-D)": "en-US-Neural2-D",
    "UK - Male (Neural2-B)": "en-GB-Neural2-B",
    "UK - Female (Neural2-C)": "en-GB-Neural2-C",
    "Australia - Male (Neural2-D)": "en-AU-Neural2-D",
    "Australia - Female (Neural2-F)": "en-AU-Neural2-F"
}
selected_voice_label = st.selectbox("Choose a voice for the podcast:", list(voice_options.keys()))
selected_voice_id = voice_options[selected_voice_label]

# --- Voice Speed
st.subheader("⚡ Voice Speed")
voice_speed = st.slider("Adjust speaking rate", min_value=0.5, max_value=2.0, value=1.0, step=0.1)

# --- Generate Script
if text_data and st.button("🎬 Generate Podcast Script"):
    with st.spinner("Generating full podcast script using Ollama/Mistral..."):
        input_word_count = len(text_data.split())
        final_script, topics = generate_podcast_script_iterative(text_data, min_words=3000)
        script_lines = final_script.splitlines()
        final_script = "\n".join(script_lines[2:])
        script_word_count = len(final_script.split())

        st.subheader("🎤 Podcast Script")
        st.text_area("Script", final_script, height=300)
        st.markdown(f"**📝 Input word count:** {input_word_count} words")
        st.markdown(f"**🗣️ Script word count:** {script_word_count} words")

        if script_word_count < 0.5 * input_word_count:
            st.warning("⚠️ The script appears shorter than expected based on input length. Consider regenerating.")

        st.download_button(
            label="💾 Download Script as TXT",
            data=final_script,
            file_name="podcast_script.txt",
            mime="text/plain"
        )

        srt_script = ""
        for i, line in enumerate(final_script.strip().split('\n')):
            if line.strip():
                srt_script += f"{i+1}\n00:00:{i:02d},000 --> 00:00:{i+1:02d},000\n{line.strip()}\n\n"

        st.download_button(
            label="🎬 Download Script as SRT (subtitles)",
            data=srt_script,
            file_name="podcast_script.srt",
            mime="text/plain"
        )

        # Save script for later use
        st.session_state['podcast_script'] = final_script

# --- Generate Audio
if 'podcast_script' in st.session_state:
    st.subheader("🔊 Convert Script to Audio")
    if st.button("🎧 Generate MP3"):
        with st.spinner("Generating audio with Google Cloud TTS..."):
            timestamp = int(time.time())
            output_mp3 = f"podcast_audio_{timestamp}.mp3"
            text_to_speech(st.session_state['podcast_script'], output_mp3, selected_voice_id, voice_speed)

            with open(output_mp3, "rb") as f:
                st.download_button(
                    label="📥 Download Podcast MP3",
                    data=f.read(),
                    file_name=output_mp3,
                    mime="audio/mpeg"
                )

            os.remove(output_mp3)
