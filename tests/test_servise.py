import requests
import json

URL = "http://localhost:9696/predict"

with open('./tests/sample.json') as fp:
    sample = json.load(fp)

result = requests.post(URL, json=sample).json()

print(json.dumps(result))
