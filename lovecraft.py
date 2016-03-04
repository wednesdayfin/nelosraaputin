import scrapy
import random
import pyttsx

class DmozSpider(scrapy.Spider):
    name = "lovecraft"
    allowed_domains = ["goodreads.com"]
    start_urls = [
        #"https://www.goodreads.com/author/quotes/205.Robert_A_Heinlein"
        "https://www.goodreads.com/author/quotes/9494.H_P_Lovecraft"
    ]
 	

    def parse(self, response):
    	num = random.randint(0,29)
    	

	print "\nnumeroksi arpoutui: %d\n" % num
	
	#hein_lista = []
	love_lista = []
	
	#heinlein()
	
	for sel in response.xpath('//div/div/div/div/div/div/div'):
		quote = sel.xpath('div[@class="quoteText"][1]/text()').extract()
		if (len(quote) > 1):
			love_lista.append(' '.join(quote))
			 
			
	for i in love_lista:
		print "%s " % i
        
        print love_lista[num]
        engine = pyttsx.init()
    	rate = engine.getProperty('rate')
    	engine.setProperty('rate', rate - 50)
        #engine.say("Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn")
        #engine.say(love_lista[num])
        #engine.runAndWait()
        	
##to do:
#parsiminen alifunktioon?
