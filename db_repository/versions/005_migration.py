from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
drivers = Table('drivers', pre_meta,
    Column('driver_id', INTEGER, primary_key=True, nullable=False),
    Column('email', VARCHAR(length=40)),
    Column('password', VARCHAR(length=20)),
    Column('firstName', VARCHAR(length=20)),
    Column('lastName', VARCHAR(length=40)),
    Column('profilePhoto', VARCHAR(length=60)),
    Column('carPhoto', VARCHAR(length=60)),
    Column('isBusy', BOOLEAN),
    Column('carModel', VARCHAR(length=30)),
    Column('carLicense', VARCHAR(length=7)),
)

users = Table('users', pre_meta,
    Column('user_id', INTEGER, primary_key=True, nullable=False),
    Column('email', VARCHAR(length=40)),
    Column('password', VARCHAR(length=20)),
    Column('firstName', VARCHAR(length=20)),
    Column('lastName', VARCHAR(length=40)),
    Column('profilePhoto', VARCHAR(length=60)),
    Column('creditCard', VARCHAR(length=16)),
)

Drivers = Table('Drivers', post_meta,
    Column('driver_id', Integer, primary_key=True, nullable=False),
    Column('email', String(length=40)),
    Column('password', String(length=20)),
    Column('firstName', String(length=20)),
    Column('lastName', String(length=40)),
    Column('profilePhoto', String(length=60), default=ColumnDefault('')),
    Column('carPhoto', String(length=60), default=ColumnDefault('')),
    Column('isBusy', Boolean, default=ColumnDefault(True)),
    Column('carModel', String(length=30), default=ColumnDefault('')),
    Column('carLicense', String(length=7)),
)

Users = Table('Users', post_meta,
    Column('user_id', Integer, primary_key=True, nullable=False),
    Column('email', String(length=40)),
    Column('password', String(length=20)),
    Column('firstName', String(length=20)),
    Column('lastName', String(length=40)),
    Column('profilePhoto', String(length=60), default=ColumnDefault('')),
    Column('creditCard', String(length=16), default=ColumnDefault('')),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['drivers'].drop()
    pre_meta.tables['users'].drop()
    post_meta.tables['Drivers'].create()
    post_meta.tables['Users'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['drivers'].create()
    pre_meta.tables['users'].create()
    post_meta.tables['Drivers'].drop()
    post_meta.tables['Users'].drop()
