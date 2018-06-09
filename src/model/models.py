# coding: utf-8
'''
auto generated file by
sqlacodegen sqlite:///starbucks.db > models.py
used for sqlalchemy operation
In fact already deprecated in current program
That is,useless since requirement 1
'''

from sqlalchemy import Column, Integer, Table, Text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


t_sqlite_sequence = Table(
    'sqlite_sequence', metadata,
    Column('name', NullType),
    Column('seq', NullType)
)


class Starbuck(Base):
    __tablename__ = 'starbucks'

    ID = Column(Integer, primary_key=True)
    brand = Column(Text)
    store_number = Column(Text)
    store_name = Column(Text)
    ownership_type = Column(Text)
    street_address = Column(Text)
    city = Column(Text)
    stateprovince = Column(Text)
    country = Column(Text)
    postcode = Column(Text)
    phone_number = Column(Text)
    timezone = Column(Text)
    longitude = Column(Text)
    latitude = Column(Text)
