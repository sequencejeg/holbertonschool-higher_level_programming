#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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
    states = (session.query(State, City).filter(City.state_id == State.id)
              .order_by(State.id))
    for state, city in states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
