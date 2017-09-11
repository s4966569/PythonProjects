import urllib.request

url = "https://www.baidu.com/"
response1 = urllib.request.urlopen(url)
if response1.getcode() == 200:
    print("第一种方法：")
    content = response1.read()
    print(content)

request = urllib.request.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response2 = urllib.request.urlopen(request)
if response2.getcode() == 200:
    print("第二种方法")
    print(response2.read())

cookieProcessor = urllib.request.HTTPCookieProcessor()
opener = urllib.request.build_opener(cookieProcessor)
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
# response3 = opener.open(request)
if response3.getcode() == 200:
    print("第三种方法:")
    print(response3.read())
