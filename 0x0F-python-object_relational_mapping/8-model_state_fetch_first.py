#!/usr/bin/python3
""" this prints the first State object from the database hbtn_0e_6_usa """

from sys import argv
from sqlalchemy import create_engine
from model_state import State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    host = 'localhost'
    port = 3306

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
        username, passwd, host, port, db_name), pool_pre_ping=True)
    
    Session = sessionmaker(bind=engine)
    R_session = Session()
    states = R_session.query(State).order_by(State.id).first()
    R_session.close()

    if states:
        print(f"{states.id}: {states.name}")
    else:
        print('Nothing')
