import requests
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("WHAPI_TOKEN")

url = f"https://gate.whapi.cloud/messages/text?token={token}"
payload = {
    "typing_time": 3,
    "to": "5511940289184@s.whatsapp.net",
    "body": "Olá, Vinicius! Bot seguro e funcionando 🚀"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
print(response.text)
