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
    }
}
broker_address = 'iot.ceit.aut.ac.ir'  # '127.0.0.1'
broker_port = 58904  # 9998


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)
    client.publish("1", json.dumps(my_json))


def on_publish(client, userdata, result):
    print("data published \n")
    pass


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("1")
    client.publish("1", json.dumps(my_json))


def on_disconnect(client, userdata, rc):
    print("disconnected with rtn code [%d]" % (rc))


client = mqtt.Client("MQTTTest")
client.on_message = on_message
client.on_publish = on_publish
client.on_connect = on_connect
client.on_disconnect = on_disconnect

if __name__ == '__main__':
    client.connect(host=broker_address, port=broker_port)
    client.loop_forever()
