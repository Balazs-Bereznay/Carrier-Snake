from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(50), nullable = False)
    conversations = db.relationship('Conversation', backref='user')

    def __repr__(self):
        return f'<User: {self.username}>'
    
class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    partner = db.Column(db.String(50), nullable = False)
    messages = db.relationship('Message', backref='conversation')

class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    conversation_id = db.Column(db.Integer, db.ForeignKey(Conversation.id))
    content = db.Column(db.String(150), nullable = False)
    sent_date = db.Column(db.Date, nullable = False)