import scrapy

class ScratchQuotes(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self,response):
        for quote in response.css(".quote"):
            yield {
                'author': quote.css('.author::text').get(),
                'quotes':quote.css('.text::text').get(),
                'tags': quote.css("div.tags a::text").getall()
            }

        nextPageURL = response.css('li.next a::attr(href)').get()

        if nextPageURL is not None:
            yield response.follow(nextPageURL, callback=self.parse)