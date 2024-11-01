#!/usr/bin/python3

'''This script prints all states that has a letter a'''

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
    state_name = sys.argv[4]
    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print('Not found')
    session.close()
