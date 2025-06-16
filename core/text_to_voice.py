# tts.py
from google.cloud import texttospeech
from pydub import AudioSegment
import io


def split_text(text, max_length=4500):
    """
    Splits the input text into chunks under Google Cloud TTS character limits using simple punctuation-based splitting.
    """
    if not text:
        return []

    sentences = text.split('. ')
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        sentence += ". "  # Re-append the dot
        if len(current_chunk) + len(sentence) <= max_length:
            current_chunk += sentence
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks


def text_to_speech(text, output_path, voice_id="en-US-Neural2-F", speaking_rate=1.0):
    """
    Converts text to speech using Google Cloud Text-to-Speech and saves it as a single MP3 file.
    """
    client = texttospeech.TextToSpeechClient()
    chunks = split_text(text)
    combined_audio = AudioSegment.empty()

    for chunk in chunks:
        input_text = texttospeech.SynthesisInput(text=chunk)
        voice = texttospeech.VoiceSelectionParams(
            language_code="-".join(voice_id.split("-")[:2]),
            name=voice_id,
            ssml_gender=texttospeech.SsmlVoiceGender.SSML_VOICE_GENDER_UNSPECIFIED
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            speaking_rate=speaking_rate
        )
        response = client.synthesize_speech(
            input=input_text,
            voice=voice,
            audio_config=audio_config
        )

        audio_segment = AudioSegment.from_file(io.BytesIO(response.audio_content), format="mp3")
        combined_audio += audio_segment

    combined_audio.export(output_path, format="mp3")
    print(f"✅ Audio saved to: {output_path}")
