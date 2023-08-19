#!/usr/bin/python3
""" This changes the name
    of a State object from
    the database hbtn_0e_6_usa
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

    state = R_session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    R_session.commit()
