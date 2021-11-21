#!/usr/bin/python
import os
import requests
import json
json_rawdata = requests.get("https://catfact.ninja/fact").json()
json_data = json.dumps(json_rawdata)
myjson = json.loads(json_data)
print("Writing to file catfacts.json...");
with open(os.path.join(os.path.dirname(__file__), 'catfacts.json'), 'w') as f:
    json.dump(json_data, f)
print("...done...");
