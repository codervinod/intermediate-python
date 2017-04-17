import os

from flask import Flask, request, url_for, abort, jsonify

app = Flask(__name__)
app.debug = True

db = {}


@app.route('/')
def show_entries():
    collections = [
        dict(href=url_for('get_collection', cname=cname), cname=cname)
        for cname in db]
    return jsonify(collections=collections)


@app.route('/<cname>', methods=['GET'])
def get_collection(cname):
    collection = db.get(cname)
    if collection is None:
        return abort(404)
    docs = [
        dict(href=url_for('get_doc', cname=cname, id=id), id=id)
        for id in collection]
    return jsonify(docs=docs)


@app.route('/<cname>', methods=['POST'])
def post_collection(cname):
    doc = request.get_json()
    collection = db.setdefault(cname, {})
    id = _gen_id()
    collection[id] = doc
    return jsonify(
        href=url_for('get_doc', cname=cname, id=id),
        id=id)


@app.route('/<cname>', methods=['DELETE'])
def drop_collection(cname):
    db.pop(cname, None)
    return jsonify()


@app.route('/<cname>/<id>', methods=['GET'])
def get_doc(cname, id):
    collection = db.get(cname)
    if collection is None:
        return abort(404)
    doc = collection.get(id)
    if doc is None:
        return abort(404)
    return jsonify(doc)


@app.route('/<cname>/<id>', methods=['PUT'])
def put_doc(cname, id):
    doc = request.get_json()
    collection = db.setdefault(cname, {})
    collection[id] = doc
    return jsonify(doc)


@app.route('/<cname>/<id>', methods=['DELETE'])
def del_doc(cname, id):
    collection = db.get(cname)
    if collection is None:
        return abort(404)
    collection.pop(id, None)
    return jsonify()


def _gen_id():
    return os.urandom(12).encode('base64').strip()


if __name__ == '__main__':
    app.run()
