#!/usr/bin/python3
"""
creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
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
    Base.metadata.create_all(engine)
    # create session and its factory
    Session = sessionmaker(bind=engine)
    session = Session()
    # create/add new state and city
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)

    session.add(new_state)
    session.add(new_city)

    session.commit()

    # close session
    session.close()
