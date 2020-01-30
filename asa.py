import requests

url = "https://192.168.10.100/api/interfaces/physical"

payload = "{\r\n\t\"ned:Loopback\": {\r\n\t\t\"name\": 200,\r\n\t\t\"ip\": {\r\n\t\t\t\"address\": {\r\n\t\t\t\t\"primary\": {\r\n\t\t\t\t\t\"address\": \"160.99.1.1\",\r\n\t\t\t\t\t\"mask\": \"255.255.255.0\"\r\n\t\t\t\t}\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n}"
headers = {
    'Content-Type': "application/vnd.yang.data+json",
    'Accept': "application/vnd.yang.data+json",
    'Authorization': "Basic ZW5hYmxlXzE6Y2lzY28="
    }

response = requests.request("GET", url, verify=False, data=payload, headers=headers)

print(response.text)
