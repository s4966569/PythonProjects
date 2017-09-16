from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Table, Column, INTEGER, String, Sequence, DATE, VARCHAR

# BaseModel = declarative_base()


class ReplyInfo:

    # __tablename__ = "tiebareply"
    # id = Column(INTEGER,primary_key=True, autoincrement=True)
    # author = Column(VARCHAR)
    # reply = Column(VARCHAR)
    # floor = Column(VARCHAR)
    # time = Column(DATE)

    def __init__(self):
        self.author = None
        self.reply = None
        self.floor = None
        self.time = None


    def __iter__(self):
        return iter([self.author, self.reply, self.floor, self.time])

    def __str__(self):
        return self.author + "(" + self.floor + "," + str(self.time) + ")" + "------" + self.reply

    def __repr__(self):
        return str(self)