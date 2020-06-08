import scrapy
from bs4 import BeautifulSoup
import re

from Ptt.items import PttItem

class PttHotSpider(scrapy.Spider):
    name = 'ptt_hot'
    start_urls = [
        'https://www.ptt.cc/bbs/index.html'
    ]
    headers = {
        'cookie':'__cfduid=de2e887ab16adce3f0238a8e8233f60051591615031; __cf_bm=5e76c3aa0100596b85bc895230f56618b79d393e-1591615732-1800-AT4UQCJb8/RbprpexwqwMh0/SsyD8T8DbaP28J7F0wQmwDPWLBaauFx345EVy7jbfv91cMAcktOm9FcEhDdcoIqpiW/2n778F8DosTnUdYZI+e9fJtD2D3yaAMomeG8jiQ==; over18=1'
    }
    domain = 'https://www.ptt.cc'
    def parse(self, response):
        # print(response.text)

        soup = BeautifulSoup(response.body, 'lxml')
        Linktags = soup.find_all('a', href = re.compile(r"index"))
        print(Linktags[0])
        print(len(Linktags))
        for tag in Linktags:
            # print(tag.text.strip().replace('\n',' '))
            soup = BeautifulSoup(str(tag), 'lxml')
            url = self.domain + tag.get('href')
            boardName = soup.select('div.board-name')[0].text
            push = soup.select('div.board-nuser')[0].text
            boardClass = soup.select('div.board-class')[0].text
            boardTitle = soup.select('div.board-title')[0].text
            print(url)
            print(boardName)
            print(push)
            print(boardClass)
            print(boardTitle)
            item = PttItem(boardlink=url , boardName=boardName, push=push, boardClass=boardClass, boardTitle=boardTitle )
            yield item
    #         yield scrapy.Request(url,cookies={'over18':'1'}, callback=self.parse_articleLink)

    # def parse_articleLink(self, response):
    #     soup = BeautifulSoup(response.body, 'lxml')
    #     tags = soup.find_all('a', href = re.compile(r"M.\d{10}"))
    #     print(len(tags))
        # for tag in tags:
        #     if tag is None:
        #         print('Link Tag Not Found')
        #     else:
        #         print('Link Tag Found')
        #         print(tag.text)
        #         print(self.domain + tag.get('href'))

