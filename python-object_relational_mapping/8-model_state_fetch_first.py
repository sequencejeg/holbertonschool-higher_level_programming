#!/usr/bin/python3
"""
This script prints the first State object from the database.
"""

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
    Below we create an engine which is how SQLAlchemy communicates
    with the database.
    """
    engine = create_engine(
        f"mysql+mysqldb://{user_name}:{password}@localhost:3306/{db_name}"
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")
