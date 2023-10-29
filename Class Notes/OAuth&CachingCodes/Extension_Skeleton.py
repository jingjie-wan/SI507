
def open_cache():
    ''' opens the cache file if it exists and loads the JSON into
    the CACHE_DICT dictionary.
    if the cache file doesn't exist, creates a new cache dictionary
    '''

def save_cache(cache_dict):
    ''' saves the current state of the cache to disk

    Called by make_request_with_cache()
    '''

def construct_unique_key(baseurl, params):
    ''' constructs a key that is guaranteed to uniquely and 
    repeatably identify an API request by its baseurl and params

    Called by make_request_with_cache()
    '''

def make_request(baseurl, params):
    '''Make a request to the Web API using the baseurl and params

    Called by make_request_with_cache()
    '''

def make_request_with_cache(baseurl, params):
    '''Check the cache for a saved result for this baseurl+params
    combo. If the result is found, return it. Otherwise send a new 
    request, save it, then return it.
    '''

CACHE_DICT = open_cache()
endpoint_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q': '@umsi'}
results = make_request_with_cache(endpoint_url, params)

tweets = results['statuses']
for t in tweets:
    print(t['text'])