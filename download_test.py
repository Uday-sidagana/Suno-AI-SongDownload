import requests
import json
import os
from dotenv import load_dotenv
import time
load_dotenv()



SUNO_API = os.getenv("SUNO_API")


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
    

get_task_result('ddcc1fb992f48224433c72a16d67b164')