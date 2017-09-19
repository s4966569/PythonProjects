from TieBaCrawler import TieBaCrawler
from DBHelper import MYSQLHelper

crawler = TieBaCrawler()
print("百度贴吧单个帖子内容抓取：\n")
# str_url = "https://tieba.baidu.com/p/5318604959" #双梦交易帖
# str_url = "https://tieba.baidu.com/p/5214246057"  #念破五毒专贴
str_url = "https://tieba.baidu.com/p/5214254168"  #念破唐门
data = crawler.fetch_post_data(str_url,from_page=50)
# data.reverse()

db_helper = MYSQLHelper()
db_helper.insert_replies(data)
db_helper.closedb()

print("========共" + str(len(data)) + "条数据========")