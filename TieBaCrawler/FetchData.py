from TieBaCrawler import TieBaCrawler
from DBHelper import MYSQLHelper

crawler = TieBaCrawler()
print("百度贴吧单个帖子内容抓取：\n")
str_url = "https://tieba.baidu.com/p/5318604959"
data = crawler.fetch_post_data(str_url)
# data.reverse()

db_helper = MYSQLHelper()
db_helper.insert_replies(data)
db_helper.closedb()

print("========共" + str(len(data)) + "条数据========")