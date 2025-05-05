import requests
import json
import os
from dotenv import load_dotenv
import time
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


# ----------------



def get_task_result(task_id):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {SUNO_API}"
    }

    payload = {
        "taskId": task_id
    }

    response = requests.post("https://apibox.erweima.ai/api/v1/get-task-result", headers=headers, json=payload)
    result = response.json()

    if result.get("code") == 200:
        return result  # task ready
    elif result.get("code") in [201, 202]:  # still processing states
        return None
    else:
        raise Exception(f"API error: {result.get('msg') or 'Unknown error'}")


#---------------

def download_music_file(music_url, filename):
    response = requests.get(music_url)
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"Downloaded to {filename}")

#---------------

result = generate_lyrics()

task_id = result["data"]["taskId"]  
print(f"Task ID: {task_id}")

while True:
    task_result = get_task_result(task_id)
    
    if task_result is None:
        print("Music not ready yet... checking again in 5 seconds")
        time.sleep(5)
        continue

    music_url = task_result["data"].get("musicUrl") if task_result.get("data") else None

    if music_url:
        print(f"Music ready: {music_url}")
        download_music_file(music_url, "Peaceful_Piano_Meditation.mp3")
        break
    else:
        print("Music not ready yet... checking again in 5 seconds")
        time.sleep(5)

#---------


