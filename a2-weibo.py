import requests
import json
from lxml import etree
from bs4 import BeautifulSoup


def parseMethod(id, html):
    if id == 'bs':
        soup = BeautifulSoup(html, 'lxml')
        sc = soup.find_all('script')[14].string
        start = sc.find("(")
        substr = sc[start + 1:-1]
        text = json.loads(substr)  # str转dict
        rxml = text["html"]  # 打印dict的key值,包含pid,js,css,html
        soupnew = BeautifulSoup(rxml, 'lxml')
        tr = soupnew.find_all('tr', attrs={'action-type': 'hover'})
    elif id == 'lxml':
        selector = etree.HTML(html)
        tt = selector.xpath('//script/text()')
        print(tt)
        htm = tt[8]
        start = htm.find("(")
        substr = htm[start + 1:-1]
        text = json.loads(substr)  # str转dict
        rxml = text["html"]  # 打印dict的key值,包含pid,js,css,html
        et = etree.HTML(rxml)
        tr = et.xpath(u'//tr[@action-type="hover"]')
    else:
        pass
    return tr


def lxmldata(tr):
    for t in tr:
        id = eval(t.find(u".//td[@class='td_01']").find(u".//em").text)
        title = t.find(u".//p[@class='star_name']").find(u".//a").text
        num = eval(t.find(u".//p[@class='star_num']").find(u".//span").text)
        yield {
            'index': id,
            'title': title,
            'num': num
        }


def bsdata(tr):
    for t in tr:
        id = eval(t.find('em').string)
        title = t.find(class_='star_name').find('a').string
        num = eval(t.find(class_='star_num').string)
        yield {
            'index': id,
            'title': title,
            'num': num
        }


def output(id, tr):
    with open("./weibohotnews.txt", "w", encoding='utf-8') as f:
        if id == 'bs':
            for i in bsdata(tr):
                f.write(str(dict(i)) + '\n')
        elif id == 'lxml':
            for i in lxmldata(tr):
                f.write(str(dict(i)) + '\n')
        else:
            pass


def main():
    url = 'http://s.weibo.com/top/summary?'
    method = 'lxml'
    # html = input(url)
    tr = parseMethod(method, url)
    output(method, tr)


main()
