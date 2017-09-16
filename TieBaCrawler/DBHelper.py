import mysql.connector
from ReplyInfo import ReplyInfo


class MYSQLHelper:

    cnx = mysql.connector.connect(user='root', password='s4200220',
                                   host='127.0.0.1', database='test')
    cnx.set_charset_collation('utf8mb4')
    cursor = cnx.cursor()

    query = ("insert into tiebareply (author, reply, floor, time) VALUES (%s, %s, %s, %s)")

    def insert_replies(self, list):
        self.cursor.executemany(self.query, list)
        self.cnx.commit()

    def closedb(self):
        self.cursor.close()
        self.cnx.close()

    def query_replies(self,count=0):
        if count==0:
            query_all = ("select author, reply, floor, time from tiebareply")
        else:
            query_all = ("select author, reply, floor, time from tiebareply limit " + str(count))
        self.cursor.execute(query_all)
        result = []
        for (author, reply, floor, time) in self.cursor:
            item = ReplyInfo()
            item.author = author
            item.reply = reply
            item.floor = floor
            item.time = time
            result.append(item)
        return result
