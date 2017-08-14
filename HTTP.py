import json
import requests

url = 'http://localhost:5000/Get'
my_json = {
    'agent_id': '2',
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
        print(data[my_json['states'][0]])
