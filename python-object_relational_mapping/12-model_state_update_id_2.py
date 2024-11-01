#!/usr/bin/python3
"""
This script changes the name of a State object from the
database hbtn_0e_6_usa
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
    states = session.get(State, 2)
    states.name = "New Mexico"
    session.commit()
    session.close()
