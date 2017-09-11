import urllib.request
from bs4 import BeautifulSoup
import re

print("百度贴吧单个帖子内容抓取：")
# str_url = "https://tieba.baidu.com/p/5295618892?pn=1"
str_url = "https://tieba.baidu.com/p/5300781385"
total_replies = 0
total_page = 0
response = urllib.request.urlopen(str_url)
if response.getcode() == 200:
    html_doc = response.read()
    soup = BeautifulSoup(html_doc, "html.parser", from_encoding="utf8")
    l_posts_num = soup.find("ul", class_="l_posts_num")
    l_reply_num = l_posts_num.find("li", class_="l_reply_num", recursive=False)
    l_reply_num_children = l_reply_num.findAll()
    total_replies = l_reply_num_children[0].get_text()
    total_page = l_reply_num_children[1].get_text()
    print("共" + total_replies + "条回复," + total_page + "页")

    left_section = soup.find("div", class_="left_section")
    core_title = left_section.find("div", class_=re.compile(r"title")).find("h3", class_=re.compile(r"title"))
    title = core_title.get_text()
    print("标题：" + title)

    p_post_list = left_section.find("div", class_="p_postlist").findChildren("div", class_=re.compile(r"l_post"))
    for p in p_post_list:
        d_name = p.find("div", class_="d_author").find("ul", class_="p_author").find("li", class_="d_name")
        user_name = d_name.get_text()

        d_post_content_main = p.find("div", class_="d_post_content_main")
        p_content = d_post_content_main .find("div", class_="p_content")
        post_content = p_content.find("cc").find("div", class_=re.compile(r"post_content"))
        content = post_content.get_text().strip()

        post__tail_wrap = d_post_content_main.find("div", re.compile("core_reply")).\
            find("div", re.compile("core_reply_tail")).find("div", class_=re.compile("post-tail-wrap"))
        tail_infos = post__tail_wrap.findAll("span", class_="tail-info")
        item0 = tail_infos[0]
        if len(item0.findChildren()) > 0:
            tail_infos.remove(item0)
        floor = tail_infos[0].get_text()
        time = tail_infos[1].get_text()

        print(user_name + "(" + floor + "," + time + ")")
        print("----" + content)

