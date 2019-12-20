#!/usr/bin/python3
"""
script that prints the State object with the name passed as argument
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
    arr = []
    for stateId in session.query(State.id)\
                          .filter(State.name == '{:s}'.format(sys.argv[4])):
        arr.append(stateId)
    try:
        print(arr[0][0])
    except:
        print("Not found")
    session.close()
