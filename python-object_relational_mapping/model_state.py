#!/usr/bin/python3
'''Class definition of a state and an instance base'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    '''state clase inheritance from declarative base'''
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
