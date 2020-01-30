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
      "cmd": "vlan 21",
      "version": 1
    },
    "id": 2
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "name Engineering",
      "version": 1
    },
    "id": 3
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "vlan 31",
      "version": 1
    },
    "id": 4
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "name HR",
      "version": 1
    },
    "id": 5
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "vlan 41",
      "version": 1
    },
    "id": 6
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "name Voice",
      "version": 1
    },
    "id": 7
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "vlan 51",
      "version": 1
    },
    "id": 8
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "name QA",
      "version": 1
    },
    "id": 9
  }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
