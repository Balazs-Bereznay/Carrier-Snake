from app import db, ma

user_convo = db.Table('user_convo',
                      db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                      db.Column('convo_id', db.Integer, db.ForeignKey('conversation.id')))

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(50), nullable = False)

    def __repr__(self):
        return f'<User: {self.username}>'
    
class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    users = db.relationship('User', secondary=user_convo, backref='conversations')
    messages = db.relationship('Message', backref='conversation')

class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    sender = db.Column(db.Integer, db.ForeignKey('user.id'))
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversation.id'))
    content = db.Column(db.String(150), nullable = False)
    sent_date = db.Column(db.Date, nullable = False)
    

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        
    username = ma.auto_field()

class MessageSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Message
    
    sender = ma.auto_field()
    content = ma.auto_field()
    sent_date = ma.auto_field()

class ConversationSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Conversation
        
    id = ma.auto_field()    
    users = ma.auto_field()
    messages = ma.List(ma.Nested(MessageSchema))