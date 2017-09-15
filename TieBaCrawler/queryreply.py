from MYSQLHelper import MYSQLHelper

dbhelper = MYSQLHelper()
data = dbhelper.query_replies()
print(data)
print("========共" + str(len(data)) + "条数据========")
dbhelper.closedb()