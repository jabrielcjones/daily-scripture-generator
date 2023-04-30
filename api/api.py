from flask import Flask, jsonify, request
from flask_cors import CORS

import logging as logger
import json
import random


app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

logger.basicConfig(filename='api.log', level=logger.DEBUG)


# GET /randomScripture
@app.route('/scripture/', methods=['GET'])
def get_random():
    '''
    Gets a random scripture
    '''

    with open('data/scriptures.json', 'r') as scriptures_file:
        scriptures = json.load(scriptures_file)

    response = jsonify(random.choice(scriptures['scriptures']))

    return response


# POST /scripture
@app.route('/scripture/', methods=['POST'])
def create_scripture():
    '''
    Add scripture to database
    '''

    with open('data/scriptures.json', 'r') as scriptures_file:
        scriptures = json.load(scriptures_file)

    logger.debug(f"request payload: {request.get_json()}")
    scriptures['scriptures'].append(request.get_json())

    with open('data/scriptures.json', 'w') as scriptures_file:
        json.dump(scriptures, scriptures_file, indent=4)

    return jsonify({"success": "true"})


# GET /scriptures
@app.route('/scriptures/')
def get_scriptures():
    '''
    Gets all scriptures
    '''

    with open('data/scriptures.json', 'r') as scriptures_file:
        scriptures = json.load(scriptures_file)

    return jsonify(scriptures)


# PUT /updateScripture
@app.route('/updateScripture/', methods=['PUT'])
def update_scripture():
    '''
    Update scripture from database
    '''

    with open('data/scriptures.json', 'r') as scriptures_file:
        scriptures = json.load(scriptures_file)

    for i in range(len(scriptures['scriptures'])):
        if scriptures['scriptures'][i]['scripture'] == request.get_json()['scripture']:
            try:
                scriptures['scriptures'][i]['scripture'] = request.get_json()[
                    'new_scripture']

            except KeyError:
                pass

            try:
                scriptures['scriptures'][i]['verse'] = request.get_json()[
                    'new_verse']

            except KeyError:
                pass

            try:
                scriptures['scriptures'][i]['action'] = request.get_json()[
                    'new_action']

            except KeyError:
                pass

            with open('data/scriptures.json', 'w') as scriptures_file:
                json.dump(scriptures, scriptures_file, indent=4)

            return jsonify('{"message": "scripture updated"}')

    return jsonify('{"message": "unable to find matching scripture"}')
    

# DELETE /deleteScripture
@app.route('/scripture/', methods=['DELETE'])
def delete_scripture():
    '''
    Delete scripture from database
    '''

    with open('data/scriptures.json', 'r') as scriptures_file:
        scriptures = json.load(scriptures_file)

    start_size = len(scriptures['scriptures'])
    scriptures['scriptures'] = list(
        filter(
            lambda x: x['scripture'] != request.get_json(),
            scriptures['scriptures']
            )
        )

    # for i in range(len(scriptures['scriptures'])):
    #     if scriptures['scriptures'][i]['scripture'] == request.get_json()['scripture']:
    #         scriptures['scriptures'].pop(i)

    if start_size > len(scriptures['scriptures']):
        with open('data/scriptures.json', 'w') as scriptures_file:
            json.dump(scriptures, scriptures_file, indent=4)

        return jsonify({"success": "true"})

    return jsonify({"success": "true", "message": "unable to find matching scripture"})


# app.run(port=5000)
