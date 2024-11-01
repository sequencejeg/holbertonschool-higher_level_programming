#!/usr/bin/python3

"""
This script fetches all the states cities and cities ids.
"""

import sys
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import Base, City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for city in session.query(City).options(joinedload(City.state))\
            .order_by(City.id).all():
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))
    session.close()
