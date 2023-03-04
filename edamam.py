import os, requests
# from pprint import pprint

apikey = os.environ['EDAMAM_KEY']
apiid = os.environ['APP_ID']

def call():
    url = 'https://api.edamam.com/api/recipes/v2'
    auth = {'Authorization': 'Bearer %s' % apikey}
    auth = {'Authorization': 'Bearer %s' % apiid}
    payload = {'count' : '10', 'dishType' : 'dessert'}

    data = requests.get(url, params=payload, headers =auth).json()
    
    print(data)