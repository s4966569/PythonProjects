import mysql.connector
from pet import Pet

cnx = mysql.connector.connect(user='root', password='s4200220',
                               host='127.0.0.1', database='test')
cursor = cnx.cursor()

p1 = Pet()
p2 = Pet()
p3 = Pet()
p4 = Pet()
pets = [p1, p2, p3, p4]

for i in range(10000):
    pets.append(p1)

query = ("select name, species, birth from pet")

# valuse_to_insert = [('buffy','Gwen','dog','m','1995-02-09',None),
#                     ('buffy', 'Gwen', 'dog', 'm', '1995-02-09', None),
#                     ('buffy', 'Gwen', 'dog', 'm', '1995-02-09', None)]
#
insert = ("insert into pet (name, owner, species, sex, birth, death) VALUES (%s, %s, %s, %s, %s, %s)")
cursor.executemany(insert,pets)
# insert = ("insert into pet (name, owner, species, sex, birth, death) VALUES ")
# va = ",".join("(%s, %s, %s, %s, %s, %s)" for _ in pets)
# insert += va
# flattened_values = [item for sublist in pets for item in sublist]
# cursor.execute(insert,flattened_values)


cursor.execute(query)

for(name, species, birth) in cursor:
    # print("{} was a {} that is born at {:%d %b %Y}".format(name, species, birth))
    print("{} is a {} that was born at {}".format(name, species, birth))

# print(p1)

cnx.commit()
cursor.close()
cnx.close()