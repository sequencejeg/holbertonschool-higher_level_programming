#!/usr/bin/python3
'''Class definition of a cities and an instance base'''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    '''Creates table for city'''
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State")
