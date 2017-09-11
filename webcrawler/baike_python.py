import urllib.request
from bs4 import BeautifulSoup

print("百度百科Python词条关键字以及链接抓取")
str_url = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
response = urllib.request.urlopen(str_url)
if response.getcode() == 200:
    html_doc = response.read()
    soup = BeautifulSoup(html_doc, "html.parser", from_encoding="utf8")
    nodes = soup.find_all("a", target="_blank")
    base_url = "https://baike.baidu.com"
    for node in nodes:
        print(node.get_text() + ":", base_url + node["href"])
