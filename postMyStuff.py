#
#	Sends a post request with the specified data to the specified URL.
#
import requests

postUrl = "http://bugs.python.org"
postData = {
	'number': 12524,
	'type': 'issue',
	'action': 'show'
}

r = requests.post(postUrl, data=postData)
print(r.text[:300] + '...')
