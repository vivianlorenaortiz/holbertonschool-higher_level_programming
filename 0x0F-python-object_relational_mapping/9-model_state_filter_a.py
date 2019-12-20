#!/usr/bin/python3
"""
script that lists all State objects that contain the letter a from the database
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import *

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    for state in session.query(State)\
            .filter(State.name.contains('a')).order_by(State.id):
            print("{}: {}".format(state.id, state.name))
    session.close()
