#!/usr/bin/python3
"""
This script lists all State objects from the database hbtn_0e_6_usa.
It takes 3 command-line arguments: MySQL username, MySQL password,
and database name.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

"""
On the 'if' condition below, we ensure the script runs only when
executed directly, and not when imported as a module.
"""
if __name__ == "__main__":
    host = "localhost"
    port = 3306
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    """
    Below we create an engine which is how SQLAlchemy
    communicates with the database.
    """
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@{host}:{port}/{db}"
    )

    """
    Here we create a configured class Session.
    """
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    """
    Below we create a Session instance.
    """
    session = Session()

    """
    Here we are querying for all State objects.
    """
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    """
    Finally, we close the session.
    """
    session.close()
