import scrapy
import random
import pyttsx

class DmozSpider(scrapy.Spider):
    name = "heinlein"
    allowed_domains = ["4chan.org"]
    start_urls = [
        "https://www.goodreads.com/author/quotes/205.Robert_A_Heinlein"
    ]
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    
    #engine.say('Progress isn\'t made by early risers. It\'s made by lazy men trying to find easier ways to do something.')
    #engine.runAndWait()
    

    def parse(self, response):
    	num = random.randint(0,9)
    	
	'''
        for sel in response.xpath('//form/div/div/div/div'):
        	title = sel.xpath('div/span[1]/text()').extract()
        	if (len(title) > 1):
        		print title[1]
        		
        print "\nnumeroksi arpoutui: %d\n" % num
        	
	for i in response.xpath('//form/div/div/div/div'):
		posti = i.xpath('blockquote/text()').extract()
		if (len(posti) > 1):
			print ' '.join(posti)
	
	''''
	
	'''
	print response.xpath('//form/div/div/div/div/div/span[1]/text()').extract()[num]
	print response.xpath('//form/div/div/div/div/blockquote/text()').extract()[num]
	'''
	print "\nnumeroksi arpoutui: %d\n" % num
	
        for sel in response.xpath('//form/div/div/div/div'):
        	title = sel.xpath('div/span[1]/text()').extract()
        	if (len(title) > 1):
        		print title[1]
##to do:
#text-to-speech
	
