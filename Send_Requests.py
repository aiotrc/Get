import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def get():
    print(request.json['agent_id'])
    print(request.json['thing_id'])
    # mqtt
    return 'FAIL'


if __name__ == '__main__':
    json = {'agent_id': '50',
            'thing_id': '100',
            'type': 'lamp',
            'states': [
                'on',
                'color'
            ]}
    url = 'http://localhost:5000/Agent'
    r = requests.post(url=url, json=json)
    print(r.text)
