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
    # For each product in the feed
    print (type(data))
    for groupSet in data['groupSet']:
        for offers in groupSet['offers']:
            for offer in offers:
                print (offer)

# Load Data to Akeneo
def load_data(akeneo_data):
    client = akeneo.Akeneo(AKENEO_HOST, AKENEO_CLIENT_ID, AKENEO_CLIENT_SECRET, AKENEO_USERNAME, AKENEO_PASSWORD)
    client.patchProducts(akeneo_data)


# Main Function
def main():
    # Load Data from JSON URL
    data = load_json_url(GUIDLE_FEED_URL)

    # Transform Data to Akeneo Format
    transform_data(data)

    # Load Data to Akeneo
    #load_data(akeneo_data)

if __name__ == "__main__":
    main()
