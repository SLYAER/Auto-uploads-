import os
import json
from google import genai
from google.genai import types

def get_ai_metadata():
    """
    Uses Google Gemini AI to act as the massive brain of the channel.
    Generates dynamic search ideas, viral titles, and tags so the videos are never boring.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[!] No GEMINI_API_KEY found. Falling back to default list.")
        import random
        shows = ["Family Guy funniest moments", "Rick and Morty best clips", "Simpsons classic jokes"]
        choice = random.choice(shows)
        return {
            "search_query": choice,
            "title": f"Top 5 {choice} Moments! 🤣 #shorts",
            "description": "Best funny moments! Subscribe for more.",
            "tags": ["funny", "animation", "shorts", "memes", "viral"]
        }
        
    client = genai.Client(api_key=api_key)
    print("🧠 Thinking of a viral video idea using Gemini AI...")
    
    prompt = """
    You are a viral YouTube Shorts channel manager. 
    Pick a popular animated cartoon or comedy show (e.g., Family Guy, South Park, Spongebob, King of the Hill, Bob's Burgers).
    Do not always pick the same one. Be completely random.
    Generate a JSON object with:
    1. "search_query": A highly specific YouTube search term to find compiled funny clips (e.g., "Peter Griffin being dumb compilation" or "Cartman best insults").
    2. "title": A highly clickable, viral YouTube Short title for a clip from this search. Under 60 characters. Include emojis and "#shorts".
    3. "description": A short engaging description.
    4. "tags": A list of 6 relevant tags without the # symbol.
    
    Return EXACTLY valid JSON, nothing else.
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
            ),
        )
        data = json.loads(response.text)
        return data
    except Exception as e:
        print(f"[AI ERROR] {e}")
        return {
            "search_query": "Family Guy funny compilation",
            "title": "Hilarious Cartoon Moments! 🤣 #shorts",
            "description": "Best funny moments! Subscribe for daily shorts.",
            "tags": ["funny", "cartoon", "shorts", "viral"]
        }
