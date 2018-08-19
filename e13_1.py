import json
import urllib.request, urllib.parse, urllib.error

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    print('Retrieving', address)
    uh = urllib.request.urlopen(address)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    break


info = json.loads(data)
counts=0
for item in info["comments"]:
    counts=counts+int(item["count"])
print("counts: ",counts)
