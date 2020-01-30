import requests
import json

"""
Modify these please
"""
url='http://192.168.10.60/ins'
switchuser='admin'
switchpassword='Passw0rd1'

myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "conf t",
      "version": 1
    },
    "id": 1
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "vlan 600",
      "version": 1
    },
    "id": 2
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "name Construction",
      "version": 1
    },
    "id": 3
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "vlan 700",
      "version": 1
    },
    "id": 4
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "name Analysis",
      "version": 1
    },
    "id": 5
  }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

'''
Adds network object name Development
IP address is 100.1.1.1 on ASA. Code generated using Postman
'''

url = "https://192.168.10.100/api/objects/networkobjects"

payload = "{\r\n  \"host\": {\r\n    \"kind\": \"IPv4Address\",\r\n    \"value\": \"100.1.1.1\"\r\n  },\r\n  \"kind\": \"object#NetworkObj\",\r\n  \"name\": \"Development\",\r\n  \"objectId\": \"Development\"\r\n}"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic ZW5hYmxlXzE6Y2lzY28="
    }

response = requests.request("POST", url, verify=False, data=payload, headers=headers)

print(response.text)

'''Adds static route of 216.48.1.0/24 pointing to 10.1.1.1 on IOS XE router CSR1000v'''

url = "http://192.168.10.80/restconf/api/config/native/ip/route/"

payload = "{\r\n\t\"ned:route\": {\r\n\t\t\"ip-route-interface-forwarding-list\": [{\r\n\t\t\t\"prefix\": \"216.48.1.0\",\r\n\t\t\t\"mask\": \"255.255.255.0\",\r\n\t\t\t\"fwd-list\": [{\r\n\t\t\t\t\"fwd\": \"10.1.1.1\"\r\n\t\t\t}]\r\n\t\t}],\r\n\t\t\"static\": {}\r\n\t}\r\n}"
headers = {
    'Content-Type': "application/vnd.yang.data+json",
    'Accept': "application/vnd.yang.data+json",
    'Authorization': "Basic YWRtaW46Y2lzY28="
    }

response = requests.request("PATCH", url, verify=False, data=payload, headers=headers)

print(response.text)
