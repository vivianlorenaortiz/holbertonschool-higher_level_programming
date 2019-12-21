#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import *

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1],  sys.argv[2], sys.argv[3]))
    new_state = State(name="Louisiana")
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    session.add(new_state)
    new_state_added = session.query(State)\
                             .filter_by(name=new_state.name).first()
    print(new_state_added.id)
    session.commit()
    session.close()
