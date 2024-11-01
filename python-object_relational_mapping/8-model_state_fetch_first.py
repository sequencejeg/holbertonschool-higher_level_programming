#!/usr/bin/python3

'''This script prints the first state in table states'''

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
    first_state = session.query(State).filter(State.id == 1).first()
    if first_state:
        print(f'{first_state.id}: {first_state.name}')
    else:
        print('Nothing')
    session.close()
