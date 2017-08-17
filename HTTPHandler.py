"""
We handle HTTP here
When a request comes, we publish a request to MQTT and wait for response,
then return the response in HTTP again!
"""
from flask import Flask, request
from Get import http_address, http_port, agent_connection_time, max_id
from MQTTHandler import client, get_result
import json
import time

app = Flask(__name__)


@app.route('/Get', methods=['POST'])
def get():
    """
    It calls when a request come from user
    note1: If requests are more than max, returns 'Too Many Requests Error'
    note2: If requests response takes more than max, returns 'Request Timeout Error'
    :return:a json as an str
    """
    i = 0
    while agent_connection_time[i]:  # finding an empty place in array
        i = i + 1
        if i >= max_id:
            return '429'  # Too Many Requests
    agent_connection_time[i] = time.time()

    req = request.json
    req['id'] = i  # setting an id to the request
    client.publish('agent', json.dumps(req))  # publishing the request for MQTT

    while agent_connection_time[i] and (get_result() == {} or get_result()['id'] != i):
        pass

    if not agent_connection_time[i]:
        return '408'  # Request Timeout

    result = {}
    for i in range(len(request.json['states'])):  # Separating keys that requested
        result[request.json['states'][i]] = get_result()[request.json['states'][i]]
    return json.dumps(result)


@app.errorhandler(404)
def page_not_found():
    """
    :return:404 error when url is invalid
    """
    return '404'  # Page Not Found


if __name__ == '__main__':
    app.run(host=http_address, port=http_port)
