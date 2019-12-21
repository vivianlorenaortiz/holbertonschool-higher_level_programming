#!/usr/bin/python3
"""
 Update a state
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import *

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1],  sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    state_with_id_2 = session.query(State).filter_by(id=2).first()
    state_with_id_2.name = "New Mexico"
    session.commit()
    session.close()
