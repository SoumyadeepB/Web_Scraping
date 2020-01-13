import scrapy

class Comics(scrapy.Spider):
    name='comics'

    start_urls = ['https://www.fanfiction.net/comic/']

    def parse(self,response):
        for comic in response.xpath("//div[@id='list_output']//a"):
            yield {
                'link': comic.xpath('@href').extract()[0],
                # go one level back and access text()
                'name': comic.xpath('@title').extract()
            }
