# ollama_script.py

import requests
import time

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"  # Change this if using another model

def call_llm(prompt, max_tokens=1024, temperature=0.7):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": temperature,
                    "max_tokens": max_tokens
                }
            },
            timeout=120
        )
        response.raise_for_status()
        result = response.json()
        if "response" not in result:
            raise Exception(f"Missing 'response' in Ollama output: {result}")
        return result["response"].strip()
    except Exception as e:
        print(f"LLM call failed: {e}")
        return ""

def extract_topics(text, n_topics=5):
    prompt = (
        f"Extract the {n_topics} most important topics from the following text. "
        "Return ONLY a numbered list of the topics, one per line.\n\n"
        f"{text[:]}"
    )
    result = call_llm(prompt)
    topics = [line.split('.', 1)[-1].strip() for line in result.strip().split('\n') if line]
    topics = [t for t in topics if t and not t.lower().startswith('introduction')]
    return topics[:n_topics]

def generate_intro(topics):
    prompt = (
        "Write a long, engaging podcast introduction of about 400 words. Greet listeners warmly, "
        "give a sense of the podcast's mission, tease some interesting facts or questions, "
        "and clearly list the topics for today's episode in a way that builds anticipation. "
        "Make the intro lively and inviting, and connect personally to the listener."
        "\n\nToday's topics are: "
        + ", ".join(topics) + ".\n\nNo headings or labels."
    )
    return call_llm(prompt, max_tokens=950)

def generate_topic_segment(topic, main_text):
    prompt = (
        f"Write an in-depth, engaging podcast segment of about 1000 words about '{topic}', "
        "explaining it as if to a smart but non-expert listener. Dive deep, use rich examples, stories, or analogies where possible. "
        "Focus only on this topic, using relevant insights from the provided text below, but do not summarize the entire document or mention other topics.\n\n"
        f"Text:\n{main_text[:2000]}\n"
        "No headings, labels, or closing remarks. Make it detailed, clear, and captivating."
    )
    return call_llm(prompt, max_tokens=1400)

def generate_interlude(topic1, topic2):
    prompt = (
        f"Write a brief interlude or reflection (about 200 words) that smoothly transitions the podcast discussion "
        f"from '{topic1}' to '{topic2}'. Mention what was just explored, spark curiosity for what's next, and "
        "make the transition feel natural and conversational. No headings or labels."
    )
    return call_llm(prompt, max_tokens=800)

def generate_conclusion(topics):
    prompt = (
        "Write a long, memorable podcast conclusion of about 400 words. Briefly recap what was discussed for each topic: "
        + ", ".join(topics) +
        ". Reflect on the episode's key insights, invite listeners to think further or take action, thank them sincerely, "
        "and sign off in a warm, personable way. No labels or headings."
    )
    return call_llm(prompt, max_tokens=800)

def polish_script(script):
    prompt = (
        "Polish the following podcast script so it reads as a single, flowing monologue. "
        "Smooth transitions, eliminate repetition, enhance engagement, and make it sound like a natural solo narration. "
        "Do NOT add any labels or headings.\n\n"
        + script
    )
    return call_llm(prompt, max_tokens=2048)

def expand_script(script, multiplier=2):
    prompt = (
        f"Take the following podcast script and expand it to at least {multiplier} times its current length. "
        "Add more stories, analogies, technical details, background info, deeper explanations, engaging asides, and extra narrative elements. "
        "Make it even more detailed, lively, and memorable, while preserving the original style and structure. "
        "Do not summarize; instead, elaborate thoroughly and richly.\n\n"
        f"{script}"
    )
    # Large max_tokens to allow for much longer output
    return call_llm(prompt, max_tokens=4096)

def count_words(text):
    return len(text.strip().split())

def generate_podcast_script_iterative(text, min_words=5000, n_topics=5, expand_multiplier=2, max_expansions=2):
    topics = extract_topics(text, n_topics=n_topics)
    intro = generate_intro(topics)
    segments = []
    for i, topic in enumerate(topics):
        segment = generate_topic_segment(topic, text)
        segments.append(segment)
        if i < len(topics) - 1:
            interlude = generate_interlude(topic, topics[i+1])
            segments.append(interlude)
    conclusion = generate_conclusion(topics)
    # Stitch
    raw_script = "\n\n".join([intro] + segments + [conclusion])
    polished = polish_script(raw_script)
    script = polished

    # Expansion phase to reach desired word count
    expansions = 0
    while count_words(script) < min_words and expansions < max_expansions:
        print(f"Expanding script (iteration {expansions+1}) to reach minimum {min_words} words...")
        script = expand_script(script, multiplier=expand_multiplier)
        expansions += 1
        time.sleep(1)  # avoid hammering Ollama if used in a loop

    final_word_count = count_words(script)
    print(f"Final script word count: {final_word_count}")
    return script, topics

# Example usage (Uncomment for local testing):
# text = open("your_transcript.txt").read()
# script, topics = generate_podcast_script_iterative(text)
# print(script)
