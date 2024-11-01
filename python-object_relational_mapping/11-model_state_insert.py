#!/usr/bin/python3
"""
This script we create a new State with the name "Louisiana".
”"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """
    On the 'if' condition below, we ensure the script runs only when
    executed directly, and not when imported as a module.
    """
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """
    Below we create engine that connects to the core (MySQL).
    """
    engine = create_engine(
        f"mysql+mysqldb://{user_name}:{password}@localhost:3306/{db_name}"
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    """
    This below creates new state.
    """
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    """
    Here we print new state id.
    """
    print(new_state.id)
