# tools/podcast_tool.py

from ollama_script import generate_podcast_script_iterative
from input_parser import extract_text_from_url, extract_text_from_pdf, extract_text_from_txt

def podcast_from_url(url: str) -> str:
    text = extract_text_from_url(url)
    script, _ = generate_podcast_script_iterative(text, min_words=3000)
    return script[:1200]

def podcast_from_pdf_path(pdf_path: str) -> str:
    text = extract_text_from_pdf(pdf_path)
    script, _ = generate_podcast_script_iterative(text, min_words=3000)
    return script[:1200]

def podcast_from_txt_path(txt_path: str) -> str:
    text = extract_text_from_txt(txt_path)
    script, _ = generate_podcast_script_iterative(text, min_words=3000)
    return script[:1200]
