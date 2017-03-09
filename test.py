import requests
import json
req = requests.post("http://kamalaldin.com:3000/send?hi=true", json = {"name": "kamal"})

print(req)
