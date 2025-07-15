import requests

url = "https://gate.whapi.cloud/messages/text?token=oE1fMpqQ2CFRpT2nUxkAmWU9ZFFxDZ1Y"
payload = {
    "typing_time": 3,
    "to": "5511940289184@s.whatsapp.net",
    "body": "Olá, Vinicius! Bot funcionando 🚀"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
print(response.text)
