import json
import logging as logger
import random

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

logger.basicConfig(filename='api.log', level=logger.DEBUG)


# GET /scripture
@app.route('/scripture/', methods=['GET'])
def get_scripture():
    '''
    Gets a random scripture
    '''

    with open('data/scriptures.json', 'r') as scriptures_file:
        scriptures = json.load(scriptures_file)

    response = jsonify(random.choice(scriptures['scriptures']))

    return response


# POST /scripture
@app.route('/scripture/', methods=['POST'])
def add_scripture():
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
@app.route('/scripture/verse', methods=['PUT'])
def update_verse():
    '''
    Update scripture from database
    '''

    updated = False

    with open('data/scriptures.json', 'r') as scriptures_file:
        scriptures = json.load(scriptures_file)

    for scripture in scriptures['scriptures']:
        if scripture['scripture'] != request.get_json()['scripture']:
            continue

        logger.info(f"Updating '{request.get_json()['scripture']}' verse")
        logger.debug(f"Current verse '{scripture['verse']}' verse")
        logger.debug(f"New verse '{request.get_json()['updated_verse']}' verse")
        scripture['verse'] = request.get_json()['updated_verse']
        updated = True
        logger.debug(f"Current verse '{scripture['verse']}' verse")

    if updated:
        with open('data/scriptures.json', 'w') as scriptures_file:
            json.dump(scriptures, scriptures_file, indent=4)

        return jsonify({"success": "true", "message": "scripture updated"})

    return jsonify({"success": "true", "message": "unable to find matching scripture"})


# DELETE /deleteScripture
@app.route('/scripture/', methods=['DELETE'])
def delete_scripture():
    '''
    Delete scripture from database
    '''

    with open('data/scriptures.json', 'r') as scriptures_file:
        scriptures = json.load(scriptures_file)

    logger.info(f"Removing {request.get_json()['scripture']}")
    logger.debug(f"scripture count: {len(scriptures['scriptures'])}")
    logger.debug(
        f"scriptures: {[x['scripture'] for x in scriptures['scriptures']]}"
    )
    start_size = len(scriptures['scriptures'])
    scriptures['scriptures'] = list(
        filter(
            lambda x: x['scripture'] != request.get_json()['scripture'],
            scriptures['scriptures']
        )
    )

    logger.debug(f"scripture count: {len(scriptures['scriptures'])}")
    logger.debug(
        f"scriptures: {[x['scripture'] for x in scriptures['scriptures']]}"
    )
    if start_size > len(scriptures['scriptures']):
        logger.info(f"'{request.get_json()['scripture']}' removed")
        with open('data/scriptures.json', 'w') as scriptures_file:
            json.dump(scriptures, scriptures_file, indent=4)

        return jsonify({"success": "true"})

    logger.info(f"'{request.get_json()['scripture']}' not found")
    return jsonify({"success": "true", "message": "unable to find matching scripture"})
