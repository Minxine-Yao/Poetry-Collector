from urllib.request import urlopen
from urllib.error import  HTTPError
from bs4 import BeautifulSoup

def getPoem(poem):
    title = poem["title"]
    author = poem["author"]
    content = "暂缺"
    comment = "暂缺"
    if author == "诗经":
        minTitle = title[3:]
        # 诗经索引页
        html = urlopen("http://www.gushiwen.org/guwen/shijing.aspx")
        bsObj = BeautifulSoup(html.read(), "html.parser")
        linkDiv = bsObj.find("a", text=minTitle)
        if linkDiv:
            # 找得到这首诗
            link = linkDiv["href"]
            poem_html = urlopen(link)
            bsObj = BeautifulSoup(poem_html.read(), "html.parser")
            cotent = bsObj.find("div", class_="contson").get_text()
            comment = bsObj.find("div", class_="contyishang").findAll('p', text="注释")[1].get_text()
    else:
        # 搜索结果页
        html = urlopen("http://so.gushiwen.org/search.aspx?value="+title)
        bsObj = BeautifulSoup(html.read(), "html.parser")
        linkDiv = bsObj.find("div", class_="sons")
        if linkDiv is not None:
            # 有这首诗的信息
            link = "http://so.gushiwen.org/" + linkDiv.a["href"]
            poem_html = urlopen(link)
            bsObj = BeautifulSoup(poem_html.read(), "html.parser")
            cotent = bsObj.find("div", class_="contson").p.get_text()
            comment = bsObj.find("div", class_="contyishang").findAll('p', text="注释")[1].get_text()

    poemInfo = {
        "title": title,
        "author": author,
        "content": content,
        "comment": comment
    }

    return poemInfo