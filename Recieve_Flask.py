from flask import Flask, request
from timeit import default_timer

app = Flask(__name__)


@app.route('/Agent', methods=['POST'])
def get():
    start = default_timer()
    print(request.json['agent_id'])
    print(request.json['thing_id'])

    duration = default_timer() - start

    # mqtt
    print(duration * 1000)
    return 'FAIL'


@app.errorhandler(404)
def page_not_found():
    return 'wrong url'


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    app.run(host=host, port=port)
