"""
A TEST FILE FOR mqtt
"""
import paho.mqtt.client as mqtt
from Config import broker_address, broker_port
import json

my_json = [
    {
        'id': 0,
        'humidity': {
            'value': '28',
            'time': '2016-09-24T23:05:34Z'
        },
        'temperature': {
            'value': '24',
            'time': '2016-09-24T23:05:34Z'
        },
        'something': {
            'value': 'sth',
            'time': 'some time'
        }
    },
    {
        'id': 1,
        'humidity': {
            'value': '0',
            'time': '2016-09-24T23:05:34Z'
        },
        'temperature': {
            'value': '0',
            'time': '2016-09-24T23:05:34Z'
        },
        'something': {
            'value': 'sth',
            'time': 'some time'
        }
    }
]


def on_message(client, userdata, message):
    print('Message')
    req = json.loads(message.payload.decode('utf-8'))
    for j in my_json:
        if j['id'] == req['id']:
            client.publish('get', json.dumps(j))
            return
    client.publish('get', '{}')


def on_publish(client, userdata, result):
    print('Publish')
    pass


def on_connect(client, userdata, flags, rc):
    print('Connect')
    client.subscribe('agent')


def on_disconnect(client, userdata, rc):
    print('Disconnect')
    pass


client = mqtt.Client('MQTTTest')
client.on_message = on_message
client.on_publish = on_publish
client.on_connect = on_connect
client.on_disconnect = on_disconnect

if __name__ == '__main__':
    client.connect(host=broker_address, port=broker_port)
    client.loop_forever()
