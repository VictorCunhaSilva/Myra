import scrapy
from scrapy.http import FormRequest
#from scrapy.utils.response import open_in_browser #Usado apenas para testar o login.
from ..items import MyratestItem
from scrapy.spiders import CrawlSpider


class QuotesSpider(CrawlSpider):
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
        
        page = response.url.split("/")[-2]
        
        tags = 'life'
        authors = 'Mark Twain'
        words = 'truth'
        
        for quote in quotes_div:
            if ( quote.css('.author::text').get() in authors ) and ( tags in quote.css('.tag::text').extract() ):
                text = quote.css('span.text::text').extract()
                author = quote.css('.author::text').extract()
                tag = quote.css('.tag::text').extract()
                
                items['text'] = text
                items['author'] = author
                items['tag'] = tag
                items['page'] = page
                items['rule'] = 1
                yield items
            
            if ( words in quote.css('span.text::text').get() ):
                text = quote.css('span.text::text').extract()
                author = quote.css('.author::text').extract()
                tag = quote.css('.tag::text').extract()
                
                items['text'] = text
                items['author'] = author
                items['tag'] = tag
                items['page'] = page
                items['rule'] = 2
                yield items
            
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback= self.scrap_content)