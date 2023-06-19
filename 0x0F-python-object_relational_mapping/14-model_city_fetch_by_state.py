#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""

from model_state import Base, State
from model_city import City
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
    states = session.query(State.name, City.id, City.name).filter(
            State.id == City.state_id).order_by(City.id)
    # print results
    for s in states:
        print("{:s}: ({:d}) {:s}".format(s[0], s[1], s[2]))

    # close session
    session.close()
