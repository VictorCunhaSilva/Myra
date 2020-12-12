import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

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
        }, callback=self.start_scraping)
    def start_scraping(self, response):
        open_in_browser(response)
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')