import scrapy

class Books(scrapy.Spider):
    name='books'
    start_urls = ['https://www.fanfiction.net/book/']
    
    def parse(self,response):
        book_list = dict()
        i=0
        for book in response.xpath("//div[@id='list_output']//a"):
            i=i+1
            if(i>10):
                break
            title = str(book.xpath('@title').extract())
            link = str(book.xpath('@href').extract()[0])
            book_list[title] = link

           
        yield book_list
