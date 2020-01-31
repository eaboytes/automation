'''
Challenge is to write a script that creates the following:
Tenant: acme
Application Profile: Accounting
EPG: Payroll
EPG: Bills
Process used was to use the API advisor in the apic
copy the url into postman and the payload into th ebody
Used the "Code" link to generate Python code
Also had to use the cookie from the login script and substitute using
the following script
cookie = {"APIC-cookie" : tokenfromlogin}
and also the line cookies=cookie in the response line
'''

import requests
import json

url = "http://192.168.10.1/api/aaaLogin.json"

payload = "{\n\t\"aaaUser\": {\n\t\t\"attributes\":{\n\t\t\t\"name\": \"admin\"\n\t\t\t\"pwd\" : \"ciscoapic\"\n\t\t}\n\t}\n}"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic YWRtaW46Y2lzY29hcGlj"
    }

response = requests.request("POST", url, data=payload, headers=headers)
json_response = json.loads(response.text)
print(response.text)
tokenfromlogin = (json_response)['imdata'][0]['aaaLogin']['attributes']['token']

#Create Tenant Acme

url = "http://192.168.10.1/api/node/mo/uni/tn-acme.json"

payload = "{\"fvTenant\":{\"attributes\":{\"dn\":\"uni/tn-acme\",\"name\":\"acme\",\"rn\":\"tn-acme\",\"status\":\"created\"},\"children\":[]}}"
cookie = {"APIC-cookie" : tokenfromlogin}
headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic YWRtaW46Y2lzY29hcGlj"
    }
response = requests.request("POST", url, verify=False, data=payload, headers=headers, cookies=cookie)

print(response.text)



#Create Accounting Application profile

url = "https://192.168.10.1/api/node/mo/uni/tn-acme/ap-Accounting.json"

payload = "{\"fvAp\":{\"attributes\":{\"dn\":\"uni/tn-acme/ap-Accounting\",\"name\":\"Accounting\",\"rn\":\"ap-Accounting\",\"status\":\"created\"},\"children\":[]}}"
cookie = {"APIC-cookie" : tokenfromlogin}
headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic YWRtaW46Y2lzY29hcGlj"
    }

response = requests.request("POST", url, verify=False, data=payload, headers=headers, cookies=cookie)

print(response.text)


#Create Payroll EPG
url = "https://192.168.10.1/api/node/mo/uni/tn-acme/ap-Accounting/epg-Payroll.json"

payload = "{\"fvAEPg\":{\"attributes\":{\"dn\":\"uni/tn-acme/ap-Accounting/epg-Payroll\",\"name\":\"Payroll\",\"rn\":\"epg-Payroll\",\"status\":\"created\"},\"children\":[{\"fvCrtrn\":{\"attributes\":{\"dn\":\"uni/tn-acme/ap-Accounting/epg-Payroll/crtrn\",\"name\":\"default\",\"rn\":\"crtrn\",\"status\":\"created,modified\"},\"children\":[]}},{\"fvRsBd\":{\"attributes\":{\"tnFvBDName\":\"default\",\"status\":\"created,modified\"},\"children\":[]}}]}}"
cookie = {"APIC-cookie" : tokenfromlogin}
headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic YWRtaW46Y2lzY29hcGlj"
    }

response = requests.request("POST", url, verify=False, data=payload, headers=headers, cookies=cookie)

print(response.text)

#Create Bills EPG
url = "https://192.168.10.1/api/node/mo/uni/tn-acme/ap-Accounting/epg-Bills.json"

payload = "{\"fvAEPg\":{\"attributes\":{\"dn\":\"uni/tn-acme/ap-Accounting/epg-Bills\",\"name\":\"Bills\",\"rn\":\"epg-Bills\",\"status\":\"created\"},\"children\":[{\"fvCrtrn\":{\"attributes\":{\"dn\":\"uni/tn-acme/ap-Accounting/epg-Bills/crtrn\",\"name\":\"default\",\"rn\":\"crtrn\",\"status\":\"created,modified\"},\"children\":[]}},{\"fvRsBd\":{\"attributes\":{\"tnFvBDName\":\"default\",\"status\":\"created,modified\"},\"children\":[]}}]}}"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic YWRtaW46Y2lzY29hcGlj"
    }

response = requests.request("POST", url, verify=False, data=payload, headers=headers, cookies=cookie)

print(response.text)
