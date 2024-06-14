import requests
import sys
import json #allow python to interpret json files


response =  requests.get(f'https://itunes.apple.com/search?entity=song&limit=2&term=ccc')
print(json.dumps(response.json(), indent=2))


o = response.json()
for result in o['results']:
    print(result['trackName'])

   