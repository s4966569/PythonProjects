from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class SQLALchemyHelper:

    connect_str = "mysql+mysqlconnector://root:s4200220@127.0.0.1/test?charset=utf8mb4"
    engine = create_engine(connect_str)
    connection = engine.connect()

    Session = sessionmaker(bind=engine)
    session = Session()
