#!/usr/bin/python3
""" This adds the State object
    “Louisiana” to the database
    hbtn_0e_6_usa
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

    New_state = State(name="Louisiana")
    R_session.add(New_state)
    R_session.commit()
    print(New_state.id)
