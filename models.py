from app import db


class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column('user_id', db.Integer, primary_key=True)
    email = db.Column('email', db.String(40), unique=True, index=True)
    password = db.Column('password', db.String(20), index=True)
    firstName = db.Column('firstName', db.String(20), index=True)
    lastName = db.Column('lastName', db.String(40), index=True)
    profilePhoto = db.Column('profilePhoto', db.String(60), index=True, default='')
    creditCard = db.Column('creditCard', db.String(16), index=True, default='')
    #un usuario puede tener asociadas muchas valoraciones
    userRates = db.relationship('Rates', backref='Users', lazy='dynamic')
    #un usuario puede tener asociadas muchas carreras
    userRides = db.relationship('Rides', backref='Users', lazy='dynamic')

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
        return '<id %r>, <Email %r>, <Password %r>, <First Name %r>, <Last Name %r>, <Profile Photo %r>, <Credit Card Number %r>' % (str(self.id), self.email, self.password, self.firstName, self.lastName, self.profilePhoto, self.creditCard)


class Drivers(db.Model):
    __tablename__ = 'Drivers'
    id = db.Column('driver_id', db.Integer, primary_key=True)
    email = db.Column('email', db.String(40), unique=True, index=True)
    password = db.Column('password', db.String(20), index=True)
    firstName = db.Column('firstName', db.String(20), index=True)
    lastName = db.Column('lastName', db.String(40), index=True)
    profilePhoto = db.Column('profilePhoto', db.String(60), index=True, default='')
    carPhoto = db.Column('carPhoto', db.String(60), index=True, default='')
    isBusy = db.Column('isBusy', db.Boolean(), index=True, default=True)
    carModel = db.Column('carModel', db.String(30), index=True, default='')
    carLicense = db.Column('carLicense', db.String(7), unique=True, index=True)
    driverRates = db.relationship('Rates', backref='Drivers', lazy='dynamic')
    driverRides = db.relationship('Rides', backref='Drivers', lazy='dynamic')

    def __repr__(self):
        return '<id %r>, <Email %r>, <Password %r>, <First Name %r>, <Last Name %r>, <Profile Photo %r>, <Car Photo %r>, <Is Busy %r>, <Car Model %r>, <Car License %r>' % (str(self.id), self.email, self.password, self.firstName, self.lastName, self.profilePhoto, self.carPhoto, str(self.isBusy), self.carModel, self.carLicense)


class Rates(db.Model):
    __tablename__ = 'Rates'
    id = db.Column('rate_id', db.Integer, primary_key=True)
    rate = db.Column('rate', db.Float(4), index=True)
    #la valoracion esta asociada a un usuario
    idUser = db.Column(db.Integer, db.ForeignKey('Users.user_id'))
    #la valoracion esta asociada a un conductor
    idDriver = db.Column(db.Integer, db.ForeignKey('Drivers.driver_id'))

    def __repr__(self):
        return '<Id Post %r>, <Rate %r>, <Id User %r>, <Id Driver %r>' % (str(self.id), str(self.rate), str(self.idUser), str(self.idDriver))


class Rides(db.Model):
    __tablename__ = 'Rides'
    id = db.Column('ride_id', db.Integer, primary_key=True)
    startPoint = db.Column('startPoint', db.String(50), index=True)
    endPoint = db.Column('endPoint', db.String(50), index=True)
    expectedTimeMin = db.Column('expectedTimeMin', db.Integer, index=True)
    cost = db.Column('cost', db.Float(4), index=True)
    tip = db.Column('tip', db.Float(4), index=True, default=0.0)
    creditCard = db.Column('creditCard', db.String(16), index=True)
    # una carrera esta asociada a un usuario
    idUser = db.Column(db.Integer, db.ForeignKey('Users.user_id'))
    # una carrera esta asociada a un conductor
    idDriver = db.Column(db.Integer, db.ForeignKey('Drivers.driver_id'))
    # una carrera esta asociada a una valoracion
    idRate = db.Column(db.Integer, db.ForeignKey('Rates.rate_id'))

    def __repr__(self): 
        return '<Id Ride %r>, <Start Point %r>, <End Point %r>, <Expected Time(min) %r>, <Cost %r>, <Tip %r>, <Credit Card %r>, <Id User %r>, <Id Driver %r>, <Id Rate %r>' % (str(self.id), self.startPoint, self.endPoint, str(self.expectedTimeMin), str(self.cost), str(self.tip), self.creditCard, str(self.idUser), str(self.idDriver), str(self.idRate))