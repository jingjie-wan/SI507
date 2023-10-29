import requests
NEWSAPI_KEY = 'THISISNOTAREALKEYPUTYOURKEYHERE'
#base_url = 'https://newsapi.org/v2/top-headlines'
base_url = 'http://newsapi.org/v2/top-headlines?country=us&q=election&apiKey=d329bd5768ca452eb36b406eb618cb7c'
response = requests.get(base_url)

#or: base_url = 'https://newsapi.org/v2/top-headlines'
#NEWSAPI =
#params = {"apiKey": NEWSAPI, "country": "us", "q": "election"}
result = response.json()
print(result)
