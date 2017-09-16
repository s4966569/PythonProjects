from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Pet import Pet
from ReplyInfo import ReplyInfo

connect_str = "mysql+mysqlconnector://root:s4200220@127.0.0.1/test?charset=utf8mb4"
engine = create_engine(connect_str,echo=True)
connection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()


# result = session.query(ReplyInfo).all()
# for row in result:
#     print(row)

p1 = Pet()
p1.name = 'honoy'
p1.owner = 'Buffy'
p1.species = 'dog'
p1.sex = 'f'
p1.birth = '1998-09-08'
p1.death = None

pets = []
for x in range(10):
    pets.append(p1)

# add a list (add_all只能add一个，不清楚为啥)
# session.add_all(p1)
# session.bulk_save_objects(pets)

#删除一个对象
# p = session.query(Pet).filter_by(name='Claws').one()
# session.delete(p)
# 两种不同的filter形式，需要注意写法
p = session.query(Pet).filter(Pet.name == 'Buffy').first()
session.commit()
print(p)


session.close()

