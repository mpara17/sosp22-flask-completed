# import flask libraries
from flask import Flask, jsonify, request
app = Flask(__name__)

# flask run -> server runs at http://127.0.0.1:[whatever your number is here]
@app.route("/")
def hello():
    return "Hello World!"

# mock JSON database of some staff's favorite cats 
fav_cats = [{'name': 'Harsh', 'breed': 'Indian Billi'},
        {'name': 'Mon', 'breed' : 'Calico'},
        {'name': 'Saurav', 'breed': 'All cats!'},
        {'name': 'Drshi', 'breed': 'Maine Coons'}]
# C R U D 
@app.route('/favcat', methods=['GET'])
def get_all_cats():
    # @TODO: get all the cat entries
    return jsonify({"all entries" : fav_cats})

@app.route('/favcat/<string:name>', methods=['GET'])
def get_one_cat(name):
    # @TODO: get only one staff and their favorite cat
    return_cat = fav_cats[0]
    for get_cat, get_staff in enumerate(fav_cats):
        if get_staff['name'] == name:
            return_cat = fav_cats[get_cat]
            return return_cat
        elif get_staff['name'] != name:
            return_cat = "entry does not exist"
    return jsonify({"this staff's favorite cat is " : return_cat})

@app.route('/favcat', methods=['POST'])
def add_cat():
    # @TODO: add a staff and their favorite cat 
    new_staff = request.get_json()
    fav_cats.append(new_staff)
    return jsonify({"new staff " : new_staff})

@app.route('/favcat/<string:name>', methods=['PUT'])
def edit_cat(name):
    # @TODO: modify an entry in JSON 
    update = request.get_json()
    for get_cat, get_staff in enumerate(fav_cats):
        if get_staff['name'] == name:
            fav_cats[get_cat] = update
    us = request.get_json()
    return jsonify({"list all cats " : fav_cats})

@app.route('/favcat/<string:name>', methods=['DELETE'])
def delete_cat(name):
    # @TODO: delete a staff and their favorite cat :(
    return_cat = fav_cats[0]
    for get_cat, get_staff in enumerate(fav_cats):
        if get_staff['name'] == name:
            del fav_cats[get_cat]
    return jsonify({"upated database " : fav_cats})
