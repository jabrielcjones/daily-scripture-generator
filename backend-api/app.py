from flask import Flask, jsonify, request, render_template

import json

app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('index.html')


# POST /scripture data: (name:)
@app.route('/scripture/', methods=['POST'])
def create_scripture():
    '''
    {
        scripture :
            {
                verse: "",
                action: ""
            }
    }
    '''
    request_data = request.get_json()

    # print(request_data.keys())

    # scriptures.scriptures[request_data.keys()[0]] = {
    #     'verse': request_data[request_data.keys()[0]]['verse'],
    #     'action': request_data[request_data.keys()[0]]['action']
    # }

    for key in request_data.keys():
        scripture_key = key

        scriptures.scriptures[key] = {
            'verse': request_data[key]['verse'],
            'action': request_data[key]['action']
        }

    new_scripture = {}

    new_scripture[scripture_key] = scriptures.scriptures[scripture_key]

    return jsonify(new_scripture)


# GET /store/<string:name>
# @app.route('/store/<string:name>')
# def get_store(name):
#     for store in stores:
#         if name == store['name']:
#             return jsonify(store)

#     return jsonify({'message': 'store not found'})


# GET /scripture
@app.route('/scripture/')
def get_scriptures():
    with open('scriptures.json', 'r') as scriptures_file:
        scriptures = json.load(scriptures_file)

    return jsonify(scriptures)


# # POST /store/<string:name>/item (name:, price:)
# @app.route('/store/<string:name>/item', methods=['POST'])
# def create_item_in_store(name):
#     request_data = request.get_json()

#     for store in stores:
#         if name == store['name']:

#             new_item = {
#                 'name': request_data['name'],
#                 'price': request_data['price']
#             }

#             store['items'].append(new_item)
#             return jsonify(new_item)

#     return jsonify({'message': 'store not found'})


# GET /store/<string:name>/item
# @app.route('/store/<string:name>/item')
# def get_items_in_store(name):
#     for store in stores:
#         if name == store['name']:
#             return jsonify({'items': store['items']})

#     return jsonify({'message': 'store not found'})


app.run(port=5000)
