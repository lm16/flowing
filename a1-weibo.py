import scrapy
import json
from bs4 import BeautifulSoup
from scrapy.selector import Selector
from lxml import etree

class WbSpider(scrapy.spiders.Spider):
    name = "weibo"
    allowed_domains = ["s.weibo.com/"]
    start_urls = "https://s.weibo.com/top/summary?cate=realtimehot"

    def parse(self, response):
        print(response)
        rhtml = response.xpath('//script/text()').extract()
        htm = rhtml[8]
        start = htm.find("(")
        substr = htm[start + 1:-1]
        text = json.loads(substr)
        self.getData(text["html"])

    def getData(self, text):
        soup = BeautifulSoup(text, 'lxml')
        tag = soup.select('tr[action-type="hover"]')
        for t in tag:
            index = t.find('em').string
            keyword = t.find("p", class_="star_name").a.string
            href = t.find("p", class_="star_name").a.get('href')
            isnew = t.find("p", class_="star_name").a.i
            if (isnew != None):
                isnew_str = isnew.string
            else:
                isnew_str = ""

            searchs = t.find("p", class_="star_num").span.string
            print(index, keyword, href, isnew_str, searchs)
            print("=======================================")


def main():
    wb = WbSpider()
    wb.parse(etree.HTML(wb.start_urls))

main()
