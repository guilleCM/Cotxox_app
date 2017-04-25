from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(20), unique=True, index=True)
    password = db.Column('password', db.String(20))
    email = db.Column('email', db.String(20))
    nombre = db.Column('nombre', db.String(20))
    apellidos = db.Column('apellidos', db.String(40))
    fotoPerfil = db.Column('fotoPerfil', db.String(60))
    saldo = db.Column('saldo', db.Float(2))
    idTarjeta = db.Column('tarjeta', db.String(20))

    def __init__(self, username, password, email, nombre, apellidos, fotoPerfil, saldo, idTarjeta):
        self.username = username
        self.password = password
        self.email = email
        self.nombre = nombre
        self.apellidos = apellidos
        self.fotoPerfil = fotoPerfil
        self.saldo = saldo
        self.idTarjeta = idTarjeta

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<id %r>, <User %r>, <Password %r>, <Email %r>, <Nombre %r>, <Apellidos %r>, <Foto Perfil %r>, <Saldo %r>, <Tarjeta %r>' % (self.id, self.username, self.password, self.email, self.nombre, self.apellidos, self.fotoPerfil, self.saldo, self.idTarjeta)