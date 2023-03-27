import urllib
import json
from akeneo import akeneo 
from dotenv import load_dotenv, find_dotenv
from os import getenv

load_dotenv(find_dotenv())

## Load from Job Environment Variables
GUIDLE_FEED_URL = getenv('GUIDLE_FEED_URL')
AKENEO_HOST = getenv('AKENEO_HOST')
AKENEO_CLIENT_ID = getenv('AKENEO_CLIENT_ID')
AKENEO_CLIENT_SECRET = getenv('AKENEO_CLIENT_SECRET')
AKENEO_USERNAME = getenv('AKENEO_USERNAME')
AKENEO_PASSWORD = getenv('AKENEO_PASSWORD')

# Extract Data from JSON URL
def load_json_url(url):
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    return data

# Transform Data to Akeneo Format
def transform_data(data):
    # Extract Data from JSON
    id = data['id']
    name = data['name']
    description = data['description']
    price = data['price']
    image = data['image']

    # Transform Data to Akeneo Format
    akeneo_data = {
        "identifier": id,
        "enabled": True,
        "family": "tshirts",
        "groups": [],
        "categories": [
            "master_catalog"
        ],
        "values": {
            "name": [
                {
                    "locale": None,
                    "scope": None,
                    "data": name
                }
            ],
            "description": [
                {
                    "locale": None,
                    "scope": None,
                    "data": description
                }
            ],
            "price": [
                {
                    "locale": None,
                    "scope": None,
                    "data": [
                        {
                            "amount": price,
                            "currency": "USD"
                        }
                    ]
                }
            ],
            "image": [
                {
                    "locale": None,
                    "scope": None,
                    "data": image
                }
            ]
        }
    }
    return akeneo_data

# Load Data to Akeneo
def load_data(akeneo_data):
    client = akeneo.Akeneo(AKENEO_HOST, AKENEO_CLIENT_ID, AKENEO_CLIENT_SECRET, AKENEO_USERNAME, AKENEO_PASSWORD)
    client.patchProducts(akeneo_data)
    