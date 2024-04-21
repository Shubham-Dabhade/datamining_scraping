import scrapy

class IMDBSpider(scrapy.Spider):
    name = "imdb"
    start_urls = ["https://www.imdb.com/chart/top/"]


    def start_requests(self):
        # alter the user agent's platform with new custom headers
        custom_headers = {
            "Sec-Ch-Ua-Platform": "\"Linux\"",
            "User-Agent": "Mozilla/5.0 (Linux; x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        }
        for url in self.start_urls:
            yield scrapy.Request(url, headers=custom_headers, callback=self.parse)

    # parse the response HTML
    def parse(self, response):
        pass
