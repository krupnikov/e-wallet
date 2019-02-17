import http.client
import json

body = json.dumps({"sender": "user7", "destination": "user2", "sum": 3})

headers = {"Content-type": "application/json",
           "Accept": "application/json"}

conn = http.client.HTTPConnection("localhost", 5000)

conn.request("POST", "", body, headers)
response = conn.getresponse()
print(response.status, response.reason)

data = response.read()
print(data)

conn.close()