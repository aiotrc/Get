from flask import Flask, request, json
from timeit import default_timer
import paho.mqtt.client as mqtt

req = '-'
JSON = {}


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)
    global JSON
    JSON = json.loads(message.payload.decode("utf-8"))
    print(JSON['humidity'])


def on_publish(client, userdata, result):
    print("data published")


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    global req
    client.subscribe(req)
    # client.publish("agent_id", "anybody there ?")


def on_disconnect(client, userdata, rc):
    print("disconnected with rtn code [%d]" % rc)


app = Flask(__name__)
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
max_duration = 10
max_id = 3
host = '127.0.0.1'
port = 5000
broker_address = 'iot.ceit.aut.ac.ir'  # '127.0.0.1'
broker_port = 58904  # 9998
agent_connection_time = [False] * max_id
client = mqtt.Client("HTTPTest")
client.on_message = on_message
client.on_publish = on_publish
client.on_connect = on_connect
client.on_disconnect = on_disconnect


@app.route('/Get', methods=['POST'])
def get():
    i = 0
    while agent_connection_time[i]:
        print(i)
        i = i + 1
        if i >= max_id:
            return '429'  # Too Many Requests
    agent_connection_time[i] = default_timer()

    # MQTT
    global req
    req = request.json['agent_id']  # TODO Correct the format
    client.subscribe(req)

    global JSON
    while default_timer() - agent_connection_time[i] < max_duration and JSON == {}:
        pass
    duration = default_timer() - agent_connection_time[i]
    agent_connection_time[i] = False
    if duration > max_duration:
        return '408'  # Request Timeout
    return json.dumps(JSON)


@app.errorhandler(404)
def page_not_found():
    return '404'  # Page Not Found


if __name__ == '__main__':
    client.connect(broker_address, broker_port)
    client.loop_start()
    app.run(host=host, port=port)
    client.loop_forever()
