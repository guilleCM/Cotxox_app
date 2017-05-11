from app import db


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column('user_id', db.Integer, primary_key=True)
    email = db.Column('email', db.String(20), unique=True, index=True)
    password = db.Column('password', db.String(20))
    firstName = db.Column('firstName', db.String(20))
    lastName = db.Column('lastName', db.String(40))
    profilePhoto = db.Column('profilePhoto', db.String(60))
    creditCard = db.Column('creditCard', db.String(16))

    def __init__(self, email, password, firstName, lastName, profilePhoto='', creditCard=''):
        self.email = email
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.profilePhoto = profilePhoto
        self.creditCard = creditCard

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
        return '<id %r>, <Email %r>, <Password %r>, <First Name %r>, <Last Name %r>, <Profile Photo %r>, <Credit Card Number %r>' % (self.id, self.email, self.password, self.firstName, self.lastName, self.profilePhoto, self.creditCard)


class Drivers(db.Model):
    __tablename__ = 'drivers'
    id = db.Column('driver_id', db.Integer, primary_key=True)
    email = db.Column('email', db.String(20), unique=True, index=True)
    password = db.Column('password', db.String(20))
    firstName = db.Column('firstName', db.String(20))
    lastName = db.Column('lastName', db.String(40))
    profilePhoto = db.Column('profilePhoto', db.String(60))
    carPhoto = db.Column('carPhoto', db.String(60))
    isBusy = db.Column('isBusy', db.Boolean())
    carModel = db.Column('carModel', db.String(30))
    carLicense = db.Column('carLicense', db.String(7), unique=True)

    def __init__(self, email, password, firstName, lastName, carLicense, profilePhoto='', carPhoto='', isBusy=False, carModel=''):
        self.email = email
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.profilePhoto = profilePhoto
        self.carPhoto = carPhoto
        self.isBusy = isBusy
        self.carModel = carModel
        self.carLicense = carLicense

    def __repr__(self):
        return '<id %r>, <Email %r>, <Password %r>, <First Name %r>, <Last Name %r>, <Profile Photo %r>, <Car Photo %r>, <Is Busy %r>, <Car Model %r>, <Car License %r>' % (self.id, self.email, self.password, self.firstName, self.lastName, self.profilePhoto, self.carPhoto, str(self.isBusy), self.carModel, self.carLicense)