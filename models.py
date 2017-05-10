from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('user_id', db.Integer, primary_key=True)
    password = db.Column('password', db.String(20))
    email = db.Column('email', db.String(20), unique=True, index=True)
    firstName = db.Column('firstName', db.String(20))
    lastName = db.Column('lastName', db.String(40))
    profilePhoto = db.Column('profilePhoto', db.String(60))
    balance = db.Column('balance', db.Float(2))
    cardNumber = db.Column('cardNumber', db.String(20))

    def __init__(self, password, email, firstName, lastName, profilePhoto='', balance=0.0, cardNumber=''):
        self.password = password
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.profilePhoto = profilePhoto
        self.balance = balance
        self.cardNumber = cardNumber

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def get_password(self):
        return self.password

    def __repr__(self):
        return '<id %r>, <Password %r>, <Email %r>, <First Name %r>, <Last Name %r>, <Profile Photo %r>, <Balance %r>, <Card Number %r>' % (self.id, self.password, self.email, self.firstName, self.lastName, self.profilePhoto, self.balance, self.cardNumber)