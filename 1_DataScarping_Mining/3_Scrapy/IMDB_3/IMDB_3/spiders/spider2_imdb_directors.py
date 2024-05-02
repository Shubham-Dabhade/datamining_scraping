import scrapy

class IMDBDirectSpider(scrapy.Spider):
    name = 'imdbRecommendation'

    start_urls = ['https://www.imdb.com/chart/top/']
    # alter the user agent's platform with new custom headers
    custom_headers = {
        "Sec-Ch-Ua-Platform": "\"Linux\"",
        "User-Agent": "Mozilla/5.0 (Linux; x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.custom_headers, callback=self.parse)

    def parse(self, response):
        i = 0

        # function to remove title number
        def titleNumber(stringTitle):
            idx = stringTitle.index(" ")
            newString = stringTitle[idx:].strip()
            return newString


        for movie in response.css("li.cli-parent"):
            if i == 11:
                break
            i+=1
            movieAnchor = movie.css("div.cli-title a.ipc-title-link-wrapper")

            movieUrl = movieAnchor.css("::attr(href)").get()
            movieName = titleNumber(movieAnchor.css("::text").get())

            dic = {
                'MovieName':movieName
            }

            yield response.follow(movieUrl,callback=self.parseMovieInfo,headers=self.custom_headers, meta=dic)


    def parseMovieInfo(self,response):
        movieDirectorAnchor = response.css('li[data-testid="title-pc-principal-credit"] a')

        movieDirectorName = movieDirectorAnchor.css("::text").get()
        movieDirectorUrl = movieDirectorAnchor.css("::attr(href)").get()

        dic = {
            'MovieName':response.meta['MovieName'],
            'MovieDirector':movieDirectorName
        }

        yield response.follow(movieDirectorUrl,callback=self.parseDirectorInfo,headers=self.custom_headers,meta = dic)


    def parseDirectorInfo(self,response):
        movie_data_div = response.css("div.lleRhy")

        movie_name = movie_data_div.css("div.ipc-primary-image-list-card__content a.ipc-primary-image-list-card__title")
        movie = movie_name.css("::text").getall()
        top_movies = ','.join(movie)

        yield {
            'MovieName':response.meta['MovieName'],
            'DirectorName':response.meta['MovieDirector'],
            'TopMovies':top_movies
        }