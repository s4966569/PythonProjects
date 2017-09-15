import mysql.connector

cnx = mysql.connector.connect(user='root', password='s4200220',
                              host='127.0.0.1', database='test')
cnx.set_charset_collation('utf8mb4')
cursor = cnx.cursor()

s = '出号有看上的直接加我就行企鹅🐧1186767688'
query = "INSERT INTO tbl_test (message) VALUES ('出号有看上的直接加我就行企鹅🐧1186767688')"

query1 = "select message from tbl_test"

cursor.execute(query)
cursor.execute(query1)

for message in cursor:
    print(message)

cursor.close()
cnx.close()
