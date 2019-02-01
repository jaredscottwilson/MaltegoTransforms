#Pivot Hash to VT Detection Count

#! python
from MaltegoTransform import *
import sys
import requests
import json


hash = sys.argv[1]
m = MaltegoTransform()

try:
	params = {'apikey': keys.VirusTotal_KEY, 'resource': hash}
	headers = {
	  "Accept-Encoding": "gzip, deflate",
	  "User-Agent" : "gzip,  My Python requests library example client or username"
	  }
	response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',
	params=params, headers=headers)
	json_response = response.json()

	if response.status_code == 200:
		m.addEntity('vt.VirusTotalDetectionCount',str(json_response['positives']))
		m.returnOutput()
	else:
		m.addEntity('vt.VirusTotalDetectionCount',0)
		m.returnOutput()
except ValueError:
	print("Oops! Invalid entry")