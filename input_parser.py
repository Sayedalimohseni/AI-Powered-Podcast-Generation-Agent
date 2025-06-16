from newspaper import Article
import PyPDF2
import os

def extract_text_from_url(url):
    """
    Downloads and extracts text content from a given URL using newspaper3k.
    """
    article = Article(url)
    article.download()
    article.parse()
    return article.text


def extract_text_from_pdf(path):
    """
    Extracts all text from a PDF file using PyPDF2.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    
    with open(path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        return "".join([page.extract_text() or "" for page in reader.pages])


def extract_text_from_txt(path):
    """
    Reads plain text from a .txt file.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    
    with open(path, "r", encoding="utf-8") as file:
        return file.read()
