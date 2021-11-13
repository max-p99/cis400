from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
from syn import *
from structs import *

app = Flask(__name__)
api = Api(app)
CORS(app)

# {"query": ["list", "of", "words", "to", "find", "synonyms"]}
@app.route('/synonyms', methods=['POST'])
def get_synonyms_list():
    content = request.json
    print(content)
    query = content['query']
    print(query)
    syns = syn(query)

    imgs = lookup(syns)

    resp = jsonify(imgs)
    resp.status_code = 200
    return resp

# {"query": ["list", "of", "tags"]}
@app.route('/findartist', methods=['POST'])
def get_artist():
    content = request.json
    query = content['query']

    shops = tattoo_shop_find(query)
    resp = jsonify(shops)
    resp.status_code = 200
    return resp

# send request to this route with something Like
# {"name": "artist_name", "tags": ["list", "of", "tags"]}
@app.route('/newartist', methods=['POST'])
def new_artist():
    content = request.json
    name = content['name']
    tags = content['tags']

    cleaned = write_shop_to_csv(name, tags)
    resp = jsonify(cleaned)
    resp.status_code = 200
    return resp


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))




if __name__ == '__main__':
    app.run(debug=True)
