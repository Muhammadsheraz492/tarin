import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    # allowed_domains = ["X"]
    start_urls = ["https://tarin.es/anillos-de-compromiso"]

    def parse(self, response):
        hrefs=response.xpath("//div[@class='uael-woo-products-thumbnail-wrap']/a/@href").extract()
        for href in hrefs:
            yield scrapy.Request(url=href, callback=self.detail)


    def detail(self,response):
        data={}
        url=response.url
        title=response.xpath("//div[@class='elementor-widget-container']/h1/text()").extract()
        price = response.xpath("//p[@class='price']/span/bdi/text()").get()
        large_image = response.xpath("//div[@class='woocommerce-product-gallery__image']/a/img/@data-large_image").get()
        data["title"]=title
        data["price"]=price
        data["large_image"]=large_image
        data["url"]=url
        yield data
