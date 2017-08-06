import requests

if __name__ == '__main__':
    url = 'http://localhost:5000/Get'
    json = {
        "agent_id": "b07882d6-5c28-597b-89f9-d250f74b0bad",
        "thing_id": "1",
        "states": [
            "temperature",
            "humidity"
        ]
    }
    r = requests.post(url=url, json=json)
    print(r.text)
