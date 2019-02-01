#Pivot Domain to URL

#! python
import sys
import requests
import json

domain = sys.argv[1]

url = "https://urlscan.io/api/v1/search/?q=domain:"+domain
try:
	response = requests.get(url)
	json_response = response.json()
	if json_response['total'] != 0:
		if 'results' in json_response.keys():
			for record in json_response['results']:
				if 'page' in record.keys():
					if 'url' in record['page']:
						m.addEntity('maltego.URL',str(record['page']['url']))
			m.returnOutput()
except ValueError:
	print("Oops! Invalid entry")
