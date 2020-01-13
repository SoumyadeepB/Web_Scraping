import scrapy

class Books(scrapy.Spider):
    name='books'

    start_urls = ['https://www.fanfiction.net/book/']
    
    def parse(self,response):
        book_list = dict()
        for book in response.xpath("//div[@id='list_output']//a"):
            book_list.update(book.xpath('@title').extract(),book.xpath('@href').extract()[0])

        print(book_list)    
        yield book_list
