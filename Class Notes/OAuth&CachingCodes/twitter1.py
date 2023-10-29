import json
import requests
from requests_oauthlib import OAuth1
import secrets

client_key = secrets.TWITTER_API_KEY
client_secret = secrets.TWITTER_API_SECRET
access_token = secrets.TWITTER_ACCESS_TOKEN
access_token_secret = secrets.TWITTER_ACCESS_TOKEN_SECRET

oauth = OAuth1(client_key,
            client_secret=client_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret)
endpoint_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q': '@umsi'}

response = requests.get(endpoint_url, 
                        params=params, 
                        auth=oauth)
print (response.status_code)