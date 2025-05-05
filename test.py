import requests
import json

url = "https://apibox.erweima.ai/api/v1/generate"

payload = json.dumps({
  "prompt": "A calm and relaxing piano track with soft melodies",
  "style": "Classical",
  "title": "Peaceful Piano Meditation",
  "customMode": True,
  "instrumental": True,
  "model": "V3_5",
  "negativeTags": "Heavy Metal, Upbeat Drums",
  "callBackUrl": "https://api.example.com/callback"
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer <token>'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)