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
        custom_headers = {
            "Sec-Ch-Ua-Platform": "\"Linux\"",
            "User-Agent": "Mozilla/5.0 (Linux; x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        }


        # function to remove title number
        def titleNumber(stringTitle):
            idx = stringTitle.index(" ")
            newString = stringTitle[idx:]
            return newString

        for movie in response.css("li.iherUv div.cli-title a"):
            archivedTitle = movie.css("::text").get()

            movieTitle = titleNumber(archivedTitle).strip()
            movieUrl =  movie.css("::attr(href)").get()

            dic = {
                "movieTitle" : movieTitle
            }

            yield response.follow(movieUrl, headers=custom_headers,callback=self.parseMovieInfo,meta=dic)



    ### This Function is called when getting NewPage Info
    def parseMovieInfo(self,response):
        topBlock = response.css("ul.cdJsTz li.ipc-inline-list__item")
        bottomBlock = response.css("div.ipc-chip-list__scroller")

        movieName = response.meta['movieTitle']
        movieRelease = topBlock.css(":nth-child(1)::text").get()
        movieDuration = topBlock.css(":nth-child(3)::text").get()
        movieGenre = ",".join(bottomBlock.css("span.ipc-chip__text::text").getall())

        yield {
            'Movie name':movieName,
            'Movie Release':movieRelease,
            'Movie Duration': movieDuration,
            'Movie Genre':movieGenre
        }
