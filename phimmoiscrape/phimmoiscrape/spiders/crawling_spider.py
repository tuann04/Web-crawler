from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = 'crawling'
    allowed_domains = ['phimmoiiz.net']
    start_urls = ['https://phimmoiiz.net/danh-sach/phim-le/']
    rules = (
        Rule(LinkExtractor(allow=(r"phimmoiiz.net/phimmoi/",),
                           restrict_xpaths='//li/a'),
                            callback='parse_item'),
        
        Rule(LinkExtractor(restrict_xpaths='//a[@rel="next"]'), follow=True),
    )

    def parse_item(self, response):
        info = response.xpath('//dl[@class="movie-dl"]/dt/text() | //dl[@class="movie-dl"]/dd/text()').getall()
        info = [i.strip() for i in info]
        yield {
            # 'url': response.url,
            'title' : response.css('title::text').get(),
            'info' : info,
            'rating' : response.css('span.num-rating::text').get()
            .replace('\n                                    ', ' '),
        }
