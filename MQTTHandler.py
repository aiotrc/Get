"""
We handle MQTT here
When a MQTT request comes, we store it in 'result'
"""
import paho.mqtt.client as mqtt
from Config import broker_address, broker_port
import json

result = {}


def on_message(client, userdata, message):
    # print('Massage')
    global result
    result = json.loads(message.payload.decode('utf-8'))  # Decoding 'result'


def on_publish(client, userdata, result):
    # print('Publish')
    pass


def on_connect(client, userdata, flags, rc):
    # print('Connect')
    client.subscribe('get')  # we subscribe on 'get'


def on_disconnect(client, userdata, rc):
    # print('Disconnect')
    pass


def get_result():
    return result


client = mqtt.Client('Get')  # Defining a client named 'Get'
client.on_message = on_message
client.on_publish = on_publish
client.on_connect = on_connect
client.on_disconnect = on_disconnect

if __name__ == '__main__':
    client.connect(broker_address, broker_port)
    client.loop_start()
    client.loop_forever()
