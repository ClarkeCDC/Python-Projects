import uuid
import requests

uuids = []
r = requests.get("https://pastebin.com/raw/yg6wWEm3")
content = r.text

x = uuid.getnode()

for i in content.split(","):
    uuids.append(i)
#fake UUID y = 8835504220143

if(str(x) in uuids):
    print("Succesful")
else:
    print("Unsuccesful")
