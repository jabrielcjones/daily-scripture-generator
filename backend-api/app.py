from flask import Flask, jsonify, request, render_template

import json
import random

app = Flask(__name__)


# GET /randomScripture
@app.route('/randomScripture/')
def get_random():
    '''
    Gets a random scripture
    '''

    with open('scriptures.json', 'r') as scriptures_file:
        scriptures = json.load(scriptures_file)

    return jsonify(random.choice(scriptures['scriptures']))


# POST /scripture
@app.route('/scripture/', methods=['POST'])
def create_scripture():
    '''
    Add scripture to database
    '''

    with open('scriptures.json', 'r') as scriptures_file:
        scriptures = json.load(scriptures_file)

    scriptures['scriptures'].append(request.get_json())

    with open('scriptures.json', 'w') as scriptures_file:
        json.dump(scriptures, scriptures_file, indent=4)

    return jsonify('{"message": "scripture added"}')


# GET /scripture
@app.route('/scripture/')
def get_scriptures():
    '''
    Gets all scriptures
    '''

    with open('scriptures.json', 'r') as scriptures_file:
        scriptures = json.load(scriptures_file)

    return jsonify(scriptures)


# PUT /updateScripture
@app.route('/updateScripture/', methods=['PUT'])
def update_scripture():
    '''
    Update scripture from database
    '''

    with open('scriptures.json', 'r') as scriptures_file:
        scriptures = json.load(scriptures_file)

    for i in range(len(scriptures['scriptures'])):
        if scriptures['scriptures'][i]['scripture'] == request.get_json()['scripture']:
            try:
                scriptures['scriptures'][i]['scripture'] = request.get_json()['new_scripture']

            except KeyError:
                pass

            try:
                scriptures['scriptures'][i]['verse'] = request.get_json()['new_verse']

            except KeyError:
                pass

            try:
                scriptures['scriptures'][i]['action'] = request.get_json()['new_action']

            except KeyError:
                pass

            with open('scriptures.json', 'w') as scriptures_file:
                json.dump(scriptures, scriptures_file, indent=4)

            return jsonify('{"message": "scripture updated"}')

    return jsonify('{"message": "unable to find matching scripture"}')


# DELETE /deleteScripture
@app.route('/deleteScripture/', methods=['DELETE'])
def delete_scripture():
    '''
    Delete scripture from database
    '''

    with open('scriptures.json', 'r') as scriptures_file:
        scriptures = json.load(scriptures_file)

    for i in range(len(scriptures['scriptures'])):
        if scriptures['scriptures'][i]['scripture'] == request.get_json()['scripture']:
            scriptures['scriptures'].pop(i)

            with open('scriptures.json', 'w') as scriptures_file:
                json.dump(scriptures, scriptures_file, indent=4)

            return jsonify('{"message": "scripture removed"}')

    return jsonify('{"message": "unable to find matching scripture"}')


app.run(port=5000)
