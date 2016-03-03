import scrapy

class DmozSpider(scrapy.Spider):
    name = "nelonen"
    allowed_domains = ["4chan.org"]
    start_urls = [
        "http://boards.4chan.org/a/"
    ]
    

    def parse(self, response):
        for sel in response.xpath('//form/div/div/div/div'):
        	title = sel.xpath('div/span[1]/text()').extract()
        	print title
        	
	for i in response.xpath('//form/div/div/div/div'):
		posti = i.xpath('blockquote/text()').extract()
		print posti

