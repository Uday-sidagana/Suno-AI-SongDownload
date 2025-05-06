import requests
import json
import os
from dotenv import load_dotenv
import time
load_dotenv()



SUNO_API = os.getenv("SUNO_API")


import requests

# Replace with your actual API key and task ID
API_KEY = SUNO_API
TASK_ID = 'ddcc1fb992f48224433c72a16d67b164'

url = f'https://api.suno.ai/api/generation/{TASK_ID}'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_KEY}'
}
payload = {
    'taskId': TASK_ID
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    result = response.json()
    # Check if the task is completed and retrieve the download URL
    if result.get('code') == 200:
        download_url = result['data'].get('downloadUrl')
        if download_url:
            print(f'Download URL: {download_url}')
        else:
            print('Download URL not available yet.')
    else:
        print(f"Task not completed. Status code: {result.get('code')}")
else:
    print(f'Failed to fetch task details. HTTP Status Code: {response.status_code}')


