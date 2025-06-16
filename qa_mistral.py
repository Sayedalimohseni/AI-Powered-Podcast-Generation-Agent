import requests

def ask_mistral_question(text, question, model="mistral"):
    """
    Given context text and a user question, returns an answer using a local Mistral LLM.
    """
    prompt = (
        "You are a helpful and knowledgeable assistant. Use the following text to answer the user's question. "
        "If the answer is not in the provided text, reply 'Sorry, I don't know based on the input.'\n\n"
        f"Context:\n{text}\n\n"
        f"Question: {question}\n\n"
        "Answer:"
    )
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.2,
                    "max_tokens": 512
                }
            },
            timeout=60
        )
        if response.ok:
            result = response.json()["response"]
            return result.strip()
        else:
            return "Error from LLM: " + response.text
    except Exception as e:
        return f"Error connecting to Ollama: {e}"
