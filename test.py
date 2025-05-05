import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()



SUNO_API = os.getenv("SUNO_API")

BASE_URL = "https://apibox.erweima.ai/api/v1/generate"

def call_suno_api(data):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {SUNO_API}"
    }
    
    response = requests.post(f"{BASE_URL}", headers=headers, json=data)
    result = response.json()
    
    if result.get("code") != 200:
        raise Exception(f"API error: {result.get('msg')}")
    
    return result

# Example: Generate lyrics
def generate_lyrics():
    payload = {
    "prompt": "A calm and relaxing piano track with soft melodies",
    "style": "Classical",
    "title": "Peaceful Piano Meditation",
    "customMode": True,
    "instrumental": True,
    "model": "V3_5",
    "negativeTags": "Heavy Metal, Upbeat Drums",
    "callBackUrl": "https://api.example.com/callback"
    }
    
    return call_suno_api(payload)

result = generate_lyrics()

if result:
    print(json.dumps(result, indent=2))