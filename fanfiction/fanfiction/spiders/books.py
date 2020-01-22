import scrapy
from ..items import BookItems
import json


class Books(scrapy.Spider):
    name = 'books'
    start_urls = ['https://www.fanfiction.net/book/']

    def parse(self, response):
        i = 0
        book_list = dict()
        # Get 10 most popular books
        for book in response.xpath("//div[@id='list_output']//a"):
            i = i+1
            if(i > 10):
                break
            title = str(book.xpath('@title').extract()[0])
            link = str(book.xpath('@href').extract()[0])
            book_list[title] = link

        f = open("books.json", "w")
        f.write(json.dumps(book_list))
        f.close()

        for title in book_list:
            print("Title:",title)
            print("URL:",book_list[title]) 

        yield book_list
