import scrapy

class HuggoBossSpider(scrapy.Spider):
    name='boss'
    start_urls = ["https://www.hugoboss.com/in/en/men/?gad_source=1&gclid=Cj0KCQjwlZixBhCoARIsAIC745DdORXXNRMmqqipPUyg09aPPho1tK8e0PccTU8NNswyvLpIyJYdrhAaAoL_EALw_wcB"]

    def parse(self,response):
        cssSel = 'a[href="https://www.hugoboss.com/in/en/men-all-categories/"] + div div.col-xl-offset-1 ul a::attr(href)'
        for url in response.css(cssSel).getall():
            #as we are getting the whole url so we use .Request as we don't need to append
            yield scrapy.Request(url,callback=self.parseProducts)
            break

    i = 1
    def parseProducts(self,response):
        for link in response.css("div.product-tile-plp__gallery-wrapper a.js-product-tile__product-image::attr(href)").getall():
            yield response.follow(link,callback=self.parseProduct)

        print("On "+str(self.i)+ " page")
        next_page = response.css("div.simplepagingbar__item--position a::attr(href)").get()
        if next_page is not None and self.i != 2:
            self.i += 1
            yield scrapy.Request(next_page,callback=self.parseProducts)


    def parseProduct(self,response):
        productName = response.css('h1.pdp-stage__header-title::text').get()
        colorList = []
        for color in response.css('a.slides__slide--color-selector span'):
            if color.css('u'):
                colorList.append(color.css('u::text').get().strip())
            else:
                colorList.append(color.css('::text').get().strip())
        colors = ", ".join(colorList)

        pictureUrls = response.css("picture.pdp-images__adaptive-picture img::attr(src)").getall()
        pictureUrls = ', '.join(pictureUrls)

        careInfo = response.css('div.pdp-stage__accordion-content div.care-info span::text').getall()
        careInfo = ', '.join(careInfo)

        yield {
            'Name':productName,
            'Colors':colors,
            'Pictures':pictureUrls,
            'CareInfo':careInfo
        }

