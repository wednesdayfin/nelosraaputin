import scrapy
import random
import pyttsx

class DmozSpider(scrapy.Spider):
    name = "nelonen"
    allowed_domains = ["4chan.org"]
    start_urls = [
        "http://boards.4chan.org/a/"
    ]
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    
    #engine.say('Progress isn\'t made by early risers. It\'s made by lazy men trying to find easier ways to do something.')
    #engine.runAndWait()
    

    def parse(self, response):
    	num = random.randint(0,9)
    	

        for sel in response.xpath('//form/div/div/div/div'):
        	title = sel.xpath('div/span[1]/text()').extract()
        	if (len(title) > 1):
        		print title[1]
        		
        print "\nnumeroksi arpoutui: %d\n" % num
        	
	for i in response.xpath('//form/div/div/div/div'):
		posti = i.xpath('blockquote/text()').extract()
		if (len(posti) > 1):
			print ' '.join(posti)

##to do:
#text-to-speech
