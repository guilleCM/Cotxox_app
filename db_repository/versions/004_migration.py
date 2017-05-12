from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
Rates = Table('Rates', pre_meta,
    Column('rate_id', INTEGER, primary_key=True, nullable=False),
    Column('rate', FLOAT),
    Column('idUser', INTEGER),
    Column('idDriver', INTEGER),
    Column('idRide', INTEGER),
)

Rides = Table('Rides', pre_meta,
    Column('ride_id', INTEGER, primary_key=True, nullable=False),
    Column('startPoint', VARCHAR(length=50)),
    Column('endPoint', VARCHAR(length=50)),
    Column('expectedTimeMin', INTEGER),
    Column('cost', FLOAT),
    Column('tip', FLOAT),
    Column('creditCard', VARCHAR(length=16)),
    Column('rate', FLOAT),
    Column('idUser', INTEGER),
    Column('idDriver', INTEGER),
    Column('idRate', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['Rates'].columns['idRide'].drop()
    pre_meta.tables['Rides'].columns['rate'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['Rates'].columns['idRide'].create()
    pre_meta.tables['Rides'].columns['rate'].create()
