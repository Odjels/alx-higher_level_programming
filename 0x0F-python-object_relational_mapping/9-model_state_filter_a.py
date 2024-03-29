#!/usr/bin/python3
""" this lists all State
    objects that contain the letter a
    from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]))

    session_maker = sessionmaker(bind=engine)
    R_session = session_maker()

    for state in R_session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}") if 'a' in state.name else ""
