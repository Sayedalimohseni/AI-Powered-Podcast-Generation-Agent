# tools/__init__.py

from langchain.tools import Tool
from tools.podcast_tool import podcast_from_url, podcast_from_pdf_path, podcast_from_txt_path

podcast_tools = [
    Tool(
        name="PodcastFromURL",
        func=podcast_from_url,
        description="Generate a podcast from a website article URL."
    ),
    Tool(
        name="PodcastFromPDF",
        func=podcast_from_pdf_path,
        description="Generate a podcast from a PDF file path."
    ),
    Tool(
        name="PodcastFromTXT",
        func=podcast_from_txt_path,
        description="Generate a podcast from a plain TXT file path."
    )
]
