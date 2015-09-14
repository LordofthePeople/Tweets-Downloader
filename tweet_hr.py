from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
import lxml.html as lh
from selenium import webdriver
from selenium import selenium
import time
import html2text



class tweethr(Spider):
	name = "tweet"

	allowed_domains = ["moneycontrol.com"]
	start_urls = [
	"http://www.moneycontrol.com/india/stockpricequote/bankspublicsector/statebankindia/SBI"
	]
	
	def __init__(self):
        	Spider.__init__(self)
        	
	
	
	
	def parse(self, response):

	   driver = webdriver.Firefox()
	   driver.get("http://www.moneycontrol.com/india/stockpricequote/bankspublicsector/statebankindia/SBI")
	   time.sleep(10)
	   content = driver.page_source
	   i=0
	   converter = html2text.HTML2Text()
       	   converter.ignore_links = True
	   doc = HtmlXPathSelector(response)
	   j=0			
	   while(j<6):							
		   
                   driver.refresh()	
		   for desc in doc.xpath("//div/span[@id='Bse_Prc_tick']").extract():
		           i=i+1		   		  
			   print ("\n*******************************************************\n")
			   print i
			   print converter.handle(desc)

		   for desc1 in doc.xpath("//div/span[@id='Nse_Prc_tick']").extract():
		           i=i+1
		   	   print ("\n*******************************************************\n")
			   print i
			   print converter.handle(desc1)
	
       		   j=j+1	
	 
           
	   return desc
