"""
We run every thing here!
"""

from Timer import timer
from HTTPHandler import app
from MQTTHandler import client
from Get import http_address, http_port, broker_address, broker_port

if __name__ == '__main__':
    timer.start()
    client.connect(broker_address, broker_port)
    client.loop_start()
    app.run(host=http_address, port=http_port)
    client.loop_forever()
