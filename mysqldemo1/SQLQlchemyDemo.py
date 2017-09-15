from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

cnn_str = "mysql+mysqlconnector://root:s4200220@127.0.0.1/test"
create_engine = create_engine(cnn_str, 3600)