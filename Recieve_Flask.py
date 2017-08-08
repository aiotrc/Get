from flask import Flask, request, json
from timeit import default_timer

app = Flask(__name__)
my_json = {
    'humidity': {
        'value': '27',
        'time': '2016-09-24T23:05:34Z'
    },
    'temperature': {
        'value': '24',
        'time': '2016-09-24T23:05:34Z'
    }
}


@app.route('/Get', methods=['POST'])
def get():
    start = default_timer()
    print(request.json['agent_id'])
    # TODO mqtt
    duration = default_timer() - start
    return json.dumps(my_json)
    # return 'Request Timeout!'


@app.errorhandler(404)
def page_not_found():
    return 'Page Not Found!'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')
