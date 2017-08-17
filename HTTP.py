"""
A TEST FILE FOR http
"""
import json
import requests

url = 'http://localhost:5000/Get'
my_json = {
    'agent_id': 'b07882d6-5c28-597b-89f9-d250f74b0bad',
    'thing_id': '1',
    'states': [
        'temperature',
        'humidity'
    ]
}

if __name__ == '__main__':
    r = requests.post(url=url, json=my_json)
    if r.text.__eq__('404'):
        print('Page Not Found')
    elif r.text.__eq__('408'):
        print('Request Timeout')
    elif r.text.__eq__('429'):
        print('Too Many Requests')
    else:
        data = json.loads(r.text)
        print(data)
