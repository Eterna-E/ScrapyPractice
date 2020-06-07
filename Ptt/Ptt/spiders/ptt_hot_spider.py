import scrapy
from bs4 import BeautifulSoup
import re

class PttHotSpider(scrapy.Spider):
    name = 'ptt_hot'
    start_urls = [
        'https://www.ptt.cc/bbs/index.html'
    ]
    def parse(self, response):
        # print(response.url)
        domain = 'https://www.ptt.cc'
        soup = BeautifulSoup(response.body, 'lxml')
        tags = soup.find_all('a', href = re.compile(r"index"))
        for tag in tags:
                print(tag.text.strip().replace('\n',' '))
                print(domain + tag.get('href'))