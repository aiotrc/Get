from flask import Flask, request
from timeit import default_timer

app = Flask(__name__)
json = {
    "humidity": {
        "value": "27",
        "time": "2016-09-24T23:05:34Z"
    },
    "temperature": {
        "value": "24",
        "time": "2016-09-24T23:05:34Z"
    }
}


@app.route('/Get', methods=['POST'])
def get():
    start = default_timer()
    duration = default_timer() - start
    print(request.json['agent_id'])
    # TODO mqtt
    return json


@app.errorhandler(404)
def page_not_found():
    return 'wrong url'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')
