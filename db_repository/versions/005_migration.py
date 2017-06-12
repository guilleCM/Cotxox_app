from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
Payments = Table('Payments', post_meta,
    Column('payment_id', Integer, primary_key=True, nullable=False),
    Column('idRide', Integer),
    Column('idDriver', Integer),
    Column('driverProfit', Float(precision=4)),
    Column('cotxoxProfit', Float(precision=4)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['Payments'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['Payments'].drop()
