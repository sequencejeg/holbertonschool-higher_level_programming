#!/usr/bin/python3
"""
This script lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
It takes 3 args: MySQL username, password, and database name.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """
    On the 'if' condition below, we ensure the script runs only
    when executed directly, and not when imported as a module.
    """
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """
    Here we create engine that connects to the core (MySQL).
    """
    engine = create_engine(
        f"mysql+mysqldb://{user_name}:{password}@localhost:3306/{db_name}"
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name.like('%a%'))
    for states in state:
        if state:
            print(f"{states.id}: {states.name}")
