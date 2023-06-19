#!/usr/bin/python3
"""
prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
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
    Base.metadata.create_all(engine)
    # create session and its factory
    Session = sessionmaker(bind=engine)
    session = Session()
    # query state objects and sort
    state = session.query(State).filter_by(name=argv[4]).first()
    # print results
    if state:
        print("{:d}".format(state.id))
    else:
        print("Not found")

    # close session
    session.close()
