from flask import Flask, request, json
from timeit import default_timer
import paho.mqtt.client as mqtt

app = Flask(__name__)
max_duration = 0.1
max_id = 10
host = '127.0.0.1'
port = 5000
broker_address = 'iot.ceit.aut.ac.ir'  # '127.0.0.1'
broker_port = 58904  # 9998
agent_connection_time = [False] * max_id
req = '-'
JSON = {}


def on_message(client, userdata, message):
    # print('Massage')
    global JSON
    JSON = json.loads(message.payload.decode('utf-8'))


def on_publish(client, userdata, result):
    # print('Publish')
    pass


def on_connect(client, userdata, flags, rc):
    # print('Connect')
    global req
    client.subscribe(req)


def on_disconnect(client, userdata, rc):
    # print('Disconnect')
    pass


client = mqtt.Client('HTTPTest')
client.on_message = on_message
client.on_publish = on_publish
client.on_connect = on_connect
client.on_disconnect = on_disconnect


@app.route('/Get', methods=['POST'])
def get():
    i = 0
    while agent_connection_time[i]:
        i = i + 1
        if i >= max_id:
            return '429'  # Too Many Requests
    agent_connection_time[i] = default_timer()

    global req
    req = request.json['agent_id']  # TODO Correct the format
    client.subscribe(req)

    global JSON
    while default_timer() - agent_connection_time[i] < max_duration and JSON == {}:
        pass
    duration = default_timer() - agent_connection_time[i]
    agent_connection_time[i] = False
    req = '-'
    client.subscribe(req)
    if duration > max_duration:
        return '408'  # Request Timeout

    result = {}
    for i in range(len(request.json['states'])):
        result[request.json['states'][i]] = JSON[request.json['states'][i]]
    return json.dumps(result)


@app.errorhandler(404)
def page_not_found():
    return '404'  # Page Not Found


if __name__ == '__main__':
    client.connect(broker_address, broker_port)
    client.loop_start()
    app.run(host=host, port=port)
    client.loop_forever()
