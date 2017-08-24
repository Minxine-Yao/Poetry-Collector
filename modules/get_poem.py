# -*- coding: UTF-8 –*-

import urllib
from urllib.request import urlopen
from urllib.error import  HTTPError
from urllib.parse import quote
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
            bsObj = BeautifulSoup(poem_html.read(), "html.parser", from_encoding="gb18030")
            content = bsObj.find("div", class_="contson").get_text("\n", strip=True)
            comment = bsObj.findAll("div", class_="contyishang")[1].findAll('p')[-1].get_text("\n", strip=True)
    else:
        # 搜索结果页
        html = urlopen(("http://so.gushiwen.org/search.aspx?value=" + quote(title)))
        bsObj = BeautifulSoup(html.read(), "html.parser")
        linkDiv = bsObj.find("div", class_="sons")
        if linkDiv is not None:
            # 有这首诗的信息
            link = "http://so.gushiwen.org/" + linkDiv.a["href"]
            poem_html = urlopen(link)
            bsObj = BeautifulSoup(poem_html.read(), "html.parser")
            content = bsObj.find("div", class_="contson").get_text("\n", strip=True)
            try:
                comment = bsObj.findAll("div", class_="contyishang")[1].findAll('p')[-1].get_text("\n", strip=True)
            except IndexError:
                print(title + "注释爬取异常")
            else:
                pass


    poemInfo = {
        "title": title,
        "author": author,
        "content": content,
        "comment": stripComment(comment)
    }

    return poemInfo

def stripComment(cmt):
    res = cmt
    if cmt == "暂缺":
        return res

    cmt = cmt[2:-2]
    # 遍历注释中的每个字符
    for pos in range(0,len(cmt)):
        if pos >= len(cmt):
            break
        if cmt[pos] == "\n":
            # 换行符后跟的不是带括号数字
            next_chr = ord(cmt[pos+1])
            if (
                chr(9312) in cmt and (next_chr > 9331 or next_chr < 9312) or
                chr(9353) in cmt and (next_chr > 9371 or next_chr < 9353) or
                "1" in cmt and (next_chr > ord("9") or next_chr < ord("1")) or
                "[1]" in cmt and next_chr != ord("[") or
                "（1）" in cmt and next_chr != ord("（") or
                "【" in cmt and next_chr != ord("【")
                ):
                    cmt = cmt[:pos] + cmt[pos+1:]
                    pos = pos - 1

    return cmt