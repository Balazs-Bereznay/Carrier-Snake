from app import app, db
from app.models import User, Conversation, Message
from flask import jsonify, redirect, request
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import datetime

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if 'token' in request.headers:
            token = request.headers['token']

        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            user = User.query.filter_by(name=data['uname']).first()

        except:
            return jsonify({'message': 'token is invalid'})
        return f(*args, **kwargs)

    return decorator

############# --- Auth endpoints --- #############
@app.route('/register', methods=['GET'])
def register():

    username = request.headers['username']
    password = request.headers['password']

    hashed_pass = generate_password_hash(password, method='sha256')

    new_user = User(username=username, password=hashed_pass)
    db.session.add(new_user)
    db.session.commit()

    token = jwt.encode({'name':username, 'exp':datetime.datetime.utcnow() + datetime.timedelta(days=20)}, app.config['SECRET_KEY'])

    return jsonify({ 'token':token })


@app.route('/login', methods=['GET'])
def login():

    username = request.headers['username']
    password = request.headers['password']

    hashed_pass = generate_password_hash(password, method='sha256')

    user = User.query.filter_by(username=username).first()

    return jsonify({'username':User.username})

############# --- Auth endpoints --- #############



############ --- Content endpoints --- ###########

############ --- Content endpoints --- ###########