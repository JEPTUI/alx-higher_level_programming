#!/usr/bin/python3
"""
lists all City objects from the database hbtn_0e_101_usa
"""

from relationship_state import Base, State
from relationship_city import City
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
    cities = session.query(City).order_by(City.id.asc()).all()
    # print results
    for city in cities:
        print("{:d}: {:s} -> {:s}".format(city.id, city.name, city.state.name))

    # close session
    session.close()
