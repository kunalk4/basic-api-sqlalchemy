from app import app, db
from app.models import User, UserSchema
from flask import jsonify, request
import json

user_schema = UserSchema()

@app.route("/user/details", methods=['POST'])
def user_details():
    data = request.get_json()
    if data['full_name'] and data['email'] and data['location']:
        existing_user=User.query.filter_by(email=data['email']).first()
        breakpoint() 
        if existing_user is not None:
            response = {
                    'message': 'user already exists'
                        }
            return jsonify(response), 403
        new_user = User(full_name=data['full_name'], email=data['email'], location=data['location'])
        db.session.add(new_user)
        db.session.commit()
        response = {
               'message': 'new user registered'
                   }
        return jsonify(response), 202
    response = {
         'status': 'error',
         'message': 'bad request body'
               }
    return jsonify(response), 400


@app.route("/user/details/<user_id>", methods=['GET'])
def get_user_details(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        response = {
                 'message': 'user does not exist'
                   }
        return jsonify(response), 404
    result = user_schema.dump(user)
    response = {
            'data': result,
           'status_code': 202
             }
    breakpoint()
    return jsonify(response)

@app.route('/')
def index():
    return 'Web App with Python Flask! Welcome to sahil app'