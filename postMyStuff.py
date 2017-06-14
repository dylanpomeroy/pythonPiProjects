#
#	Sends a post request with the specified data to the specified URL.
#
import requests
import json

postUrl = "https://arcane-atoll-39485.herokuapp.com/motion_events.json"
postData = {"motion_event":{"event": "hells world"}}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

r = requests.post(postUrl, data=json.dumps(postData), headers=headers)
print(r.text[:300] + '...')
