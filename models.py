from app import db ,app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(80))
    addresses = db.relationship("Address", back_populates="user")
    # address = db.relationship('Address', backref='User', cascade="all, delete-orphan",lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)


    def __repr__(self):
        return '<user {}>'.format(self.name)



class Address(db.Model):
    __tablename__ = 'Address'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    user = db.relationship("User", back_populates="addresses")
