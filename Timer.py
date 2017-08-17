"""
We check if request take too long to response, then we return 'Request Timeout Error'
"""
from Get import agent_connection_time, max_id, max_duration
import threading
import time


class TimeChecker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            for i in range(max_id):
                if agent_connection_time[i] and time.time() > agent_connection_time[i] +  max_duration:
                    agent_connection_time[i] = False
            time.sleep(max_duration / 10)


timer = TimeChecker()
