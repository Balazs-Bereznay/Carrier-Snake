from app import app, db
from app.models import User, Conversation, Message, ConversationSchema, UserSchema
from flask import jsonify, redirect, request, make_response
from sqlalchemy.exc import IntegrityError
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import datetime


############### --- Test --- ###############

@app.route('/check_stuff', methods=['GET'])
def check_stuff():

    conversations = Conversation.query.filter_by()

    for convo in conversations:
        print(convo.users)

    return jsonify({"message": "Whole lotta testing"})

############### --- Test --- ###############


############### --- ERROR --- ###############
@app.errorhandler(405)
def not_found(error):
    return make_response(jsonify( { 'error': 'Something went wrong!' } ), 405)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Something went wrong!' } ), 404)

@app.errorhandler(500)
def not_found(error):
    return make_response(jsonify( { 'error': 'Internal error' } ), 500)
############### --- ERROR --- ###############


############# --- Decorators --- #############
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

        except:
            return jsonify({'message': 'token is invalid'})
        return f(*args, **kwargs)

    return decorator

############# --- Decorators --- #############


############# --- Auth endpoints --- #############

@app.route('/register', methods=['GET'])
def register():

    username = request.headers['username']
    password = request.headers['password']

    hashed_pass = generate_password_hash(password, method='sha256')

    new_user = User(username=username, password=hashed_pass)
    db.session.add(new_user)
    try:
        db.session.commit()

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error":"Integrity Error occured"})

    token = jwt.encode({'name':username, 'exp':datetime.datetime.utcnow() + datetime.timedelta(days=7)}, app.config['SECRET_KEY'])

    return jsonify({ 'token':token.decode('utf-8') })


@app.route('/login', methods=['GET'])
def login():

    username = request.headers['username']
    password = request.headers['password']

    user = User.query.filter_by(username=username).first()

    if user == None:

        return jsonify({'error':'Bad credentials'})

    if check_password_hash(user.password, password):

        token = jwt.encode({'name':user.username, 'exp':datetime.datetime.utcnow() + datetime.timedelta(days=7)}, app.config['SECRET_KEY'])

        return jsonify({ 'token':token.decode('utf-8') })

    return jsonify({'error':'Bad credentials'})

@app.route('/validate_token')
@token_required
def validate_token():
    response = make_response('token is valid')
    response.headers['token'] = request.headers['token']
    
    return response

############# --- Auth endpoints --- #############


############ --- Content endpoints --- ###########

@app.route('/new_conversation', methods=['GET'])
@token_required
def new_conversation():

    token = request.headers['token']
    partner_name = request.headers['partner']

    data = jwt.decode(token, app.config['SECRET_KEY'])

    user = User.query.filter_by(username = data['name']).first()
    partner = User.query.filter_by(username = partner_name).first()

    new_convo = Conversation()
    new_convo.users.append(user)
    new_convo.users.append(partner)

    db.session.add(new_convo)
    db.session.commit()

    return jsonify({"message":"Success"})

@app.route('/get_conversations', methods=['GET'])
@token_required
def get_conversations():
    
    conversation_schema = ConversationSchema(many=True)
    
    token = request.headers['token']
    data = jwt.decode(token, app.config['SECRET_KEY'])

    user = User.query.filter_by(username = data['name']).first()
    
    
    return jsonify({"data":conversation_schema.dump(user.conversations)})

@app.route('/new_message', methods=['GET'])
@token_required
def new_message():
    
    token = request.headers['token']
    data = jwt.decode(token, app.config['SECRET_KEY'])
    user = User.query.filter_by(username = data['name']).first()
    
    data = request.get_json()
    date = datetime.datetime.strptime(data['sent_date'], r'%Y.%m.%d')
    
    message = Message(sender = user.id, conversation_id = data['conversation_id'], content = data['content'], sent_date = date)
    
    db.session.add(message)
    db.session.commit()
    
    return jsonify({"data":message.content})

@app.route('/get_users', methods=['GET'])
@token_required
def get_users():
    
    users = User.query.all()
    
    userschema = UserSchema(many=True)
    
    return jsonify({"users":userschema.dump(users)})
    
############ --- Content endpoints --- ###########