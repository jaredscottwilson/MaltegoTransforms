#Pivot on Google Analytics Account Numbers

#! python
from MaltegoTransform import *
import sys
import os
import requests
import json
import re

m = MaltegoTransform()
tracker = sys.argv[1]

try:
	data = {'query': tracker, 'type': 'GoogleAnalyticsAccountNumber'}
	headers =  {'Content-Type': 'application/json'}
	url = 'https://api.passivetotal.org/v2/trackers/search'
	response = requests.get(url, auth=(keys.RiskIQ_USERNAME, keys.RiskIQ_KEY), data=data)
	json_response = response.json()
	if 'success' in json_response:
		if json_response['success'] == True:
			for record in json_response['results']:
				if 'entity' in record:
					m.addEntity('maltego.Domain',str(record['entity']))
			m.returnOutput()
except ValueError:
	print("Oops! Invalid entry")