import json

json_file = 'data.json'

with open(json_file, 'r') as f:
    js = json.load(f)
    print(js)