from DBHelper import MYSQLHelper

db_helper = MYSQLHelper()

data = db_helper.query_replies()
db_helper.closedb()

print(data)

print("========共" + str(len(data)) + "条数据========")