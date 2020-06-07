import scrapy
from bs4 import BeautifulSoup
import re

class SinaNewsSpider(scrapy.Spider):
    name = 'sina_news'
    start_urls = [
        'https://news.sina.com.cn/'
    ]
    def parse(self, response):
        # print(response.url)
        soup = BeautifulSoup(response.body, 'lxml')
        tags = soup.find_all('a', href = re.compile(r"sina.*\d{4}-\d{2}-\d{2}.*shtml$"))
        for tag in tags:
            # print(tag.text.strip())
            # print(tag.get('href'))
            url = tag.get('href')