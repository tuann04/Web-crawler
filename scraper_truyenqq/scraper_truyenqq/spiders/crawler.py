from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = 'truyenqq_crawler'
    allowed_domains = ['truyenqqviet.com']
    start_urls = ['https://truyenqqviet.com/truyen-moi-cap-nhat/trang-1.html']
    rules = (
        Rule(LinkExtractor(
            # allow=("truyen-tranh"),
                           restrict_xpaths='//li/div[@class="book_avatar"]/a'),
                            callback='parse_item'),
        
        Rule(LinkExtractor(restrict_xpaths='//div[@class="page_redirect"]/a[last()-1]'), follow=True),
    )

    def parse_item(self, response):
        info = response.xpath('//ul[@class="list-info"]')
        yield {
            'url': response.url,
            'name' : response.xpath('//h1/text()').get(),
            'other_name' : info.xpath('//li[1]/p[2]/text()').get(),
            'author' : info.xpath('//li[@class="author row"]//p[last()]//text()').get(),
            'status' : info.xpath('//li[@class="status row"]//p[last()]//text()').get(),
            'liked' : info.xpath('//li[last()-2]/p[2]/text()').get(),
            'followed' : info.xpath('li[last()-1]/p[2]/text()').get(),
            'view' : info.xpath('//li[last()]/p[2]/text()').get(),
            'type' : response.xpath('//ul[@class="list01"]//a//text()').getall(),
            'description' : response.xpath('//div[@class="book_detail"]/div[2]/p/text()').get(),
        }
