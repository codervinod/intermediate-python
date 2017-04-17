"""Super-simple queueing system.

Just has a single URL per queue. PUT a json message to it, GET a json
message from it.
"""
from collections import defaultdict
from Queue import Queue, Empty

from flask import Flask, request, abort, jsonify

app = Flask(__name__)
app.debug = True

Qs = defaultdict(Queue)


@app.route('/', methods=['GET'])
def get_stats():
    result = dict(
        (k, q.qsize())
        for k, q in Qs.items())
    return jsonify(result)


@app.route('/<qname>', methods=['GET'])
def get_message(qname):
    q = Qs[qname]
    try:
        msg = q.get_nowait()
        return jsonify(msg)
    except Empty:
        return abort(404)


@app.route('/<qname>', methods=['PUT'])
def put_message(qname):
    q = Qs[qname]
    msg = request.get_json()
    q.put(msg)
    return jsonify({})


if __name__ == '__main__':
    app.run()
