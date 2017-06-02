from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
Rides = Table('Rides', pre_meta,
    Column('ride_id', INTEGER, primary_key=True, nullable=False),
    Column('startPoint', VARCHAR(length=50)),
    Column('endPoint', VARCHAR(length=50)),
    Column('expectedTimeMin', INTEGER),
    Column('cost', FLOAT),
    Column('tip', FLOAT),
    Column('creditCard', VARCHAR(length=16)),
    Column('idUser', INTEGER),
    Column('idDriver', INTEGER),
    Column('idRate', INTEGER),
)

Rides = Table('Rides', post_meta,
    Column('ride_id', Integer, primary_key=True, nullable=False),
    Column('startPoint', String(length=50)),
    Column('endPoint', String(length=50)),
    Column('time', Integer),
    Column('distance', Float(precision=4)),
    Column('cost', Float(precision=4)),
    Column('tip', Float(precision=4), default=ColumnDefault(0.0)),
    Column('creditCard', String(length=16)),
    Column('idUser', Integer),
    Column('idDriver', Integer),
    Column('idRate', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['Rides'].columns['expectedTimeMin'].drop()
    post_meta.tables['Rides'].columns['distance'].create()
    post_meta.tables['Rides'].columns['time'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['Rides'].columns['expectedTimeMin'].create()
    post_meta.tables['Rides'].columns['distance'].drop()
    post_meta.tables['Rides'].columns['time'].drop()
