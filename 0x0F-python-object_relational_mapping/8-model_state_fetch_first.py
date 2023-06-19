#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    # create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        user, passwd, db), pool_pre_ping=True)
    # create session and its factory
    Session = sessionmaker(bind=engine)
    session = Session()
    # query state objects and sort
    state = session.query(State).order_by(State.id.asc()).first()
    # print results
    if state:
        print("{:d}: {:s}".format(state.id, state.name))
    else:
        print("Nothing")

    # close session
    session.close()
