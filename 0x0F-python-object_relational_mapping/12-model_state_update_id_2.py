#!/usr/bin/python3
"""
changes the name of a State object from the database hbtn_0e_6_usa
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
    # change state name
    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"

    session.commit()

    # close session
    session.close()
