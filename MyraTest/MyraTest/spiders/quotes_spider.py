import scrapy
from scrapy.http import FormRequest
#from scrapy.utils.response import open_in_browser #Usado apenas para testar o login.
from ..items import MyratestItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/login',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response,formdata={
            'csrf_token' : token,
            'username' : 'teste@myra.com',
            'password' : 'testemyra'
        }, callback=self.scrap_content)

    def scrap_content(self, response):
        #open_in_browser(response) Apenas para testar se o login funcionou.
        
        items = MyratestItem()
        
        quotes_div = response.css('div.quote')
        
        for quote in quotes_div:
            text = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tag = quote.css('.tag::text').extract()
            
            items['text'] = text
            items['author'] = author
            items['tag'] = tag
            
            yield items