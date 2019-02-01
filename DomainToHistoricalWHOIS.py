#Pivot from Domains to all historical WHOIS data

#! python
from MaltegoTransform import *
import sys
import requests
import json
import keys
m = MaltegoTransform()

domain = sys.argv[1]

url = "https://api.passivetotal.org/v2/whois"
headers = {'Content-Type': 'application/json'}
params = {'query': domain, 'history': 'true', 'compact_record': 'true'}
try:
	response = requests.get(url, auth=(keys.RiskIQ_USERNAME, keys.RiskIQ_KEY), params=params, headers=headers)
	json_response = response.json()
	if json_response['success'] == True:
		for record in json_response['results']:
			if 'admin' in record.keys():
				if 'city' in record['admin'].keys():
					m.addEntity('pt.whoisCity',str(record['admin']['city']))
				if 'country' in record['admin'].keys():
					m.addEntity('pt.whoisCountry',str(record['admin']['country']))
				if 'email' in record['admin'].keys():
					m.addEntity('pt.whoisEmail',str(record['admin']['email']))
				if 'name' in record['admin'].keys():
					m.addEntity('pt.whoisName',str(record['admin']['name']))
				if 'organization' in record['admin'].keys():
					m.addEntity('pt.whoisOrganization',str(record['admin']['organization']))
				if 'postalCode' in record['admin'].keys():
					m.addEntity('pt.whoisPostalCode',str(record['admin']['postalCode']))
				if 'state' in record['admin'].keys():
					m.addEntity('pt.whoisState',str(record['admin']['state']))
				if 'street' in record['admin'].keys():
					m.addEntity('pt.whoisStreet',str(record['admin']['street']))
				if 'telephone' in record['admin'].keys():
					m.addEntity('pt.whoisTelephone',str(record['admin']['telephone']))
			if 'registrant' in record.keys():
				if 'city' in record['registrant'].keys():
					m.addEntity('pt.whoisCity',str(record['registrant']['city']))
				if 'country' in record['registrant'].keys():
					m.addEntity('pt.whoisCountry',str(record['registrant']['country']))
				if 'email' in record['registrant'].keys():
					m.addEntity('pt.whoisEmail',str(record['admin']['email']))
				if 'name' in record['registrant'].keys():
					m.addEntity('pt.whoisName',str(record['registrant']['name']))
				if 'organization' in record['registrant'].keys():
					m.addEntity('pt.whoisOrganization',str(record['registrant']['organization']))
				if 'postalCode' in record['registrant'].keys():
					m.addEntity('pt.whoisPostalCode',str(record['registrant']['postalCode']))
				if 'state' in record['registrant'].keys():
					m.addEntity('pt.whoisState',str(record['registrant']['state']))
				if 'street' in record['registrant'].keys():
					m.addEntity('pt.whoisStreet',str(record['registrant']['street']))
				if 'telephone' in record['registrant'].keys():
					m.addEntity('pt.whoisTelephone',str(record['registrant']['telephone']))
			if 'tech' in record.keys():
				if 'city' in record['tech'].keys():
					m.addEntity('pt.whoisCity',str(record['tech']['city']))
				if 'country' in record['tech'].keys():
					m.addEntity('pt.whoisCountry',str(record['tech']['country']))
				if 'email' in record['tech'].keys():
					m.addEntity('pt.whoisEmail',str(record['admin']['email']))
				if 'name' in record['tech'].keys():
					m.addEntity('pt.whoisName',str(record['tech']['name']))
				if 'organization' in record['tech'].keys():
					m.addEntity('pt.whoisOrganization',str(record['tech']['organization']))
				if 'postalCode' in record['tech'].keys():
					m.addEntity('pt.whoisPostalCode',str(record['tech']['postalCode']))
				if 'state' in record['tech'].keys():
					m.addEntity('pt.whoisState',str(record['tech']['state']))
				if 'street' in record['tech'].keys():
					m.addEntity('pt.whoisStreet',str(record['tech']['street']))
				if 'telephone' in record['tech'].keys():
					m.addEntity('pt.whoisTelephone',str(record['tech']['telephone']))
		m.returnOutput()
except ValueError:
	print("Oops! Invalid entry")
