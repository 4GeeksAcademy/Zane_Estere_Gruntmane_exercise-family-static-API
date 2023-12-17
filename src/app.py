"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def all_family_members(): 
    members = jackson_family.get_all_members()
    response_body = {
        "family": members
    }
    return jsonify(response_body), 200

@app.route('/members/', methods=['POST'])
def handle_add_member():
    json_data = request.get_json()
    required_key = ["first_name", "age", "lucky_number"]
    for key in required_key:
        if key not in json_data:
            return f"missing {key} key from request body", 400
        
    new_member = {
        "first_name" : json_data ["first_name"],
        "age" : json_data ["age"],
        "lucky_number":  json_data ["lucky_number"],
    }
    inner_member_data = jackson_family.add_member(new_member)
    return jsonify (inner_member_data ), 201

@app.route ('/members/',  methods=['DELETE'])
def handle_delete_member(id):
    
    id == "member_id"

    deleted_member = jackson_family.delete_member("member_id")

    if deleted_member:
        return jsonify({"done": True}), 200
    else: 
        return jsonify({"error": "Member not found"}), 400 
    
@app.route ('/members/', methods = ['GET'])

def  handle_get_member (id):
    response = request.get (id)
    response.json()
        

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
