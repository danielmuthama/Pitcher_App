from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

#callback function to retrieve a user when a unique identifier is passed 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    passcode = db.Column(db.String(255))

    minutepitches = db.relationship('NewPitch', backref = 'user', lazy = 'dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self, password):
        self.passcode = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.passcode, password)

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.name}'

class NewPitch(db.Model):
    __tablename__ = "minutepitches"

    id = db.Column(db.Integer, primary_key = True)
    pitchtitle = db.Column(db.String(255))
    mypitch = db.Column(db.String)
    postdate = db.Column(db.DateTime, default=datetime.utcnow)
    author = db.Column(db.String(255))
    category = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_minutepitches(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_minutepitches(cls, id):
        pitches = NewPitch.query.filter_by(pitch_id=id).all()
        return pitches

