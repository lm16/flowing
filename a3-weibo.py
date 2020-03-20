import requests
from lxml import etree

url = "https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6"
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/73.0.3683.103 Safari/537.36'}


def align(str, space):
    length = len(str.encode('gb2312'))
    space = space - length if space >= length else 0
    return str + ' ' * space


def main():
    html = etree.HTML(requests.get(url, headers=header).text)
    rank = html.xpath('//td[@class="td-01 ranktop"]/text()')
    affair = html.xpath('//td[@class="td-02"]/a/text()')
    gg = html.xpath('//td[@class="td-02"]/a/@href')

    # print(gg)
    view = html.xpath('//td[@class="td-02"]/span/text()')
    top = affair[0]
    affair = affair[1:]
    print('{0:<10}\t{1:<40}'.format("top", top))
    for i in range(0, len(affair)):
        # print("{0:<10}{1:{3}<20}{2}".format(rank[i], affair[i], view[i], chr(12288)))
        print(align(rank[i], 4), align(affair[i], 40), align(gg[i], 200), align(view[i], 10))
    print()


main()
