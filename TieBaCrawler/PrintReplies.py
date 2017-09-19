from DBHelper import MYSQLHelper
import re

db_helper = MYSQLHelper()

data = db_helper.query_replies()
db_helper.closedb()

# print(data)
p1 = re.compile("炮萝")
p2 = re.compile("糖盒子")
result = []
for item in data:
    if p1.search(item.reply) and p2.search(item.reply):
        result.append(item)

result.reverse()
for x in result:
    print(x)
print("========共" + str(len(result)) + "条数据========")