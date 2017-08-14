import paho.mqtt.client as mqtt
import json

my_json = {
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
}
broker_address = 'iot.ceit.aut.ac.ir'  # '127.0.0.1'
broker_port = 58904  # 9998
agent_id = 'b07882d6-5c28-597b-89f9-d250f74b0bad'


def on_message(client, userdata, message):
    # print('Massage')
    client.publish(agent_id, json.dumps(my_json))


def on_publish(client, userdata, result):
    # print('Publish')
    pass


def on_connect(client, userdata, flags, rc):
    # print('Connect')
    client.subscribe(agent_id)
    client.publish(agent_id, json.dumps(my_json))


def on_disconnect(client, userdata, rc):
    # print('Disconnect')
    pass


client = mqtt.Client('MQTTTest')
client.on_message = on_message
client.on_publish = on_publish
client.on_connect = on_connect
client.on_disconnect = on_disconnect

if __name__ == '__main__':
    client.connect(host=broker_address, port=broker_port)
    client.loop_forever()
