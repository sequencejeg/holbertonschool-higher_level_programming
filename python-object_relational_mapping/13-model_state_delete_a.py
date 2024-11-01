#!/usr/bin/python3

'''
    This is a script that deletes all State objects
    with a name containing the letter a from the database
'''

import sys
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state_del = session.query(State)\
        .filter(State.name.like('%a%')).all()
    for state in state_del:
        session.delete(state)
    session.commit()
