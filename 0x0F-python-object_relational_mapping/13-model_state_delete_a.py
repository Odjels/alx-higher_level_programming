#!/usr/bin/python3
""" This deletes all State
    objects with a name containing the
    letter a from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]))

    session_maker = sessionmaker(bind=engine)
    R_session = session_maker()

    states = R_session.query(State).filter(State.name.like('%a%')).all()
    [R_session.delete(state) for state in states]
    R_session.commit()
