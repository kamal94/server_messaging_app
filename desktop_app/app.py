import json
import urllib.request
with urllib.request.urlopen('http://kamalaldin.com:3000') as response:
   html = response.read().decode("utf-8") 
print(html)
print("first three letters of html:", html[:3])
o = json.loads(html) 
print(o)
print(o['a'])

