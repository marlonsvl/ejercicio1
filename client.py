from slack_sdk.webhook import WebhookClient
import requests
url = "https://webhook.site/4ed54cff-41ba-423e-9f46-b2c87408daf9"
webhook = WebhookClient(url)

response_api = requests.get("http://127.0.0.1:8000/valores/")
print(response_api)

response = webhook.send(text=response_api.json())

assert response.status_code == 200
