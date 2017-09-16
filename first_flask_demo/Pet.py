from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Table, Column, INTEGER, String, Sequence, DATE, VARCHAR


Base = declarative_base()


class Pet(Base):

    __tablename__ = "pet"

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(VARCHAR)
    owner = Column(VARCHAR)
    species = Column(VARCHAR)
    sex = Column(VARCHAR)
    birth = Column(DATE)
    death = Column(DATE)

    def __str__(self):
        return "<Pet(name='%s', owner='%s', species='%s', sex='%s', birth='%s', death='%s')"%(self.name, self.owner, self.species, self.sex, self.birth, self.death)