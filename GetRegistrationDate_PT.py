#Pivot from Domain to Domain Registration Date

#! python
from MaltegoTransform import *
import sys
import requests
import json

m = MaltegoTransform()
domain = sys.argv[1]

url = "https://api.passivetotal.org/v2/whois"
headers = {'Content-Type': 'application/json'}
params = {'query': domain, 'compact_record': 'true'}
try:
	response = requests.get(url, auth=(keys.RiskIQ_USERNAME, keys.RiskIQ_KEY), params=params, headers=headers)
	json_response = response.json()
	if response.status_code == 200:
		if 'registered' in json_response.keys():
			m.addEntity('pt.whoisRegistered',str(json_response['registered']))
			m.returnOutput()
except ValueError:
	print("Oops! Invalid entry")