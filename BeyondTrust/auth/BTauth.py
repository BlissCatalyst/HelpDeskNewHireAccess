import os
from dotenv import load_dotenv
import requests
import json

# Load environment variables
load_dotenv()

def BT_get_token():
    BT_CLIENTIDSECRET = os.getenv("BT_CLIENTIDSECRET")

    url = "https://help.ensignsupport.net/oauth2/token"
    headers = {
        "Authorization": f"Basic {BT_CLIENTIDSECRET}",
        "Content-Type": "application/json"
    }
    body = {"grant_type": "client_credentials"}

    response = requests.post(url, headers=headers, data=json.dumps(body))

    return response.json()