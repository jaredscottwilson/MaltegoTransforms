#Pivot from Domain to SSL Certs

#! python
from MaltegoTransform import *
import sys
import requests
import json

m = MaltegoTransform()
domain = sys.argv[1]

url = "https://api.passivetotal.org/v2/ssl-certificate/search"
headers = {'Content-Type': 'application/json'}
params = {'field': 'subjectCommonName', 'query': domain}
try:
	response = requests.get(url, auth=(keys.RiskIQ_USERNAME, keys.RiskIQ_KEY), params=params, headers=headers)
	json_response = response.json()
	if json_response['success'] == True:
		for records in json_response['results']:
			if 'sha1' in records.keys():
				m.addEntity('pt.sslSha1',str(records['sha1']))
			if 'issuerCommonName' in records.keys():
				m.addEntity('pt.sslIssuerCommonName',str(records['issuerCommonName']))
			if 'issueDate' in records.keys():
				m.addEntity('pt.sslIssueDate',str(records['issueDate']))
		m.returnOutput()
except ValueError:
	print("Oops! Invalid entry")
