import urllib.request
from bs4 import BeautifulSoup
import re

from PostInfo import PostInfo

html_parser = 'lxml'


def get_post_info(url):
    response = urllib.request.urlopen(url)
    if response.getcode() == 200:
        html_doc = response.read()
        soup = BeautifulSoup(html_doc, html_parser, from_encoding="utf8")
        l_posts_num = soup.find("ul", class_="l_posts_num")
        l_reply_num = l_posts_num.find("li", class_="l_reply_num", recursive=False)
        l_reply_num_children = l_reply_num.findAll()
        total_replies = l_reply_num_children[0].get_text()
        total_page = l_reply_num_children[1].get_text()

        left_section = soup.find("div", class_="left_section")
        core_title = left_section.find("div", class_=re.compile(r"title")).find("h3", class_=re.compile(r"title"))
        title = core_title.get_text()

        post_info = PostInfo()
        post_info.title = title
        post_info.total_page = total_page
        post_info.total_reply = total_replies
        return post_info


def fetch_single_page_data(url):
    response = urllib.request.urlopen(url)
    i = url.find("?pn=")
    index = url[i+4:len(url)]
    if response.getcode() == 200:
        print("\n第" + index + "页数据：====================================")
        html_doc = response.read()
        soup = BeautifulSoup(html_doc, html_parser, from_encoding="utf8")

        left_section = soup.find("div", class_="left_section")

        p_post_list = left_section.find("div", class_="p_postlist").findChildren("div", class_=re.compile(r"l_post"))
        for p in p_post_list:
            d_name = p.find("div", class_="d_author").find("ul", class_="p_author").find("li", class_="d_name")
            user_name = d_name.get_text()

            d_post_content_main = p.find("div", class_="d_post_content_main")
            p_content = d_post_content_main.find("div", class_="p_content")
            post_content = p_content.find("cc").find("div", class_=re.compile(r"post_content"))
            content = post_content.get_text().strip()

            post__tail_wrap = d_post_content_main.find("div", re.compile("core_reply")). \
                find("div", re.compile("core_reply_tail")).find("div", class_=re.compile("post-tail-wrap"))
            tail_infos = post__tail_wrap.findAll("span", class_="tail-info")
            item0 = tail_infos[0]
            if len(item0.findChildren()) > 0:
                tail_infos.remove(item0)
            floor = tail_infos[0].get_text()
            time = tail_infos[1].get_text()

            print(user_name + "(" + floor + "," + time + ")")
            print("----" + content)


def fetch_post_data(url: str, from_page=1, count=0):
    index = url.find("?pn=")
    if index == -1:
        base_url = url
    else:
        base_url = url[:index]

    post_info = get_post_info(base_url)
    title = post_info.title
    total_page = post_info.total_page
    total_reply = post_info.total_reply

    print("标题：" + title)
    print("共" + total_reply + "条回复," + total_page + "页")
#   页数从1开始,0默认抓取所有的
    if count <= 0:
        count = int(total_page)
    if from_page < 1:
        from_page = 1

    for i in range(from_page, count+from_page):
        if i <= int(total_page):
            page_url = base_url + '?pn=' + str(i)
            fetch_single_page_data(page_url)


print("百度贴吧单个帖子内容抓取：\n")
# str_url = "https://tieba.baidu.com/p/5295618892?pn=1"
str_url = "https://tieba.baidu.com/p/5300781385"
fetch_post_data(str_url, count=10)


