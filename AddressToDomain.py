#Pivot from Street Address to Domain

#! python
from MaltegoTransform import *
import sys
import requests
import json
import keys


m = MaltegoTransform()

address = sys.argv[1]

try:
	response = requests.get('https://api.passivetotal.org/v2/whois/search?query='+address+'&field=address', auth=(keys.RiskIQ_USERNAME, keys.RiskIQ_KEY))
	json_response = response.json()
	if 'results' in json_response:
		for record in json_response['results']:
			if 'domain' in record:
				m.addEntity('maltego.Domain',str(record['domain']))
		m.returnOutput()
except ValueError:
	print("Oops! Invalid entry")
