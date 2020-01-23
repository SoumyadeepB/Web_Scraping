import scrapy
from scrapy import Request
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
            url = book_list[title]
            #print("URL:", response.urljoin(url))
            yield Request(url=response.urljoin(url), callback=self.reviews, meta={'title': title})

    def reviews(self, response):
        review_list = {}  # Review Dictionary
        book_title = response.meta['title']
        # List of tags for each element (To allow a JSON dump)
        review_list[book_title] = []
        titles = []
        authors = []
        texts = []
        print("* Review for :: ", book_title)

        for title in response.xpath('//*[@id="content_wrapper_inner"]/div[position()>3]/a[1]/text()').extract():
            titles.append(title)

        for author in response.xpath('//*[@id="content_wrapper_inner"]/div[position()>3]/a[3]/text()').extract():
            authors.append(author)

        for text in response.xpath('//*[@id="content_wrapper_inner"]/div[position()>3]/div/text()').extract():
            texts.append(text)

        limit = 15
        for i in range(limit):
            review_list[book_title].append({
                'title': titles[i],
                'author': authors[i],
                'text': texts[i]
            })
        f = open(book_title+".json", "w")
        f.write(json.dumps(review_list[book_title]))
        f.close()
        yield review_list
