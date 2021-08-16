from flask import Blueprint, jsonify, request
from datetime import datetime as dt
from .models import User
from . import db


home = Blueprint(
    'home_bp',
    __name__
)

@home.route("/")
def hehe():
    return "more organized routes :)"

@home.route("/user/all", methods=['GET', 'DELETE'])
def all_users():
    if request.method == 'GET':
        users = User.query.all()
        user_json = {}
        for user in users:
            user_json['username'] = user.username
            user_json['created'] = user.created
        return jsonify(user_json)
    elif request.method == 'DELETE':
        try:
            users = User.query.all()
            db.session.delete(users)
            db.session.commit()
            return "Deleted the whole record."
        except:
            db.rollback()
            return "Issue batch deleting"


@home.route("/user", methods=['POST'])
def signup():
    try:
        test = User(
            username='john',
            created=dt.now()
        )
        db.session.add(test)
        db.session.commit()
        return "Signed successfully."
    except Exception as e:
        db.session.rollback()
        return "Error creating."
