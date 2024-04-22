import scrapy


class GameCrawlerSpider(scrapy.Spider):
    name = "game_crawler"
    allowed_domains = ["en.wikipedia.org"]
    custom_settings = {
        'DEPTH_LIMIT': 3,
        'MAX_PAGES': 300
    }
    start_urls = ["https://en.wikipedia.org/wiki/Video_game"]


    def __int__(self, *args, **kwargs):
        super(GameCrawlerSpider, self).__init__(*args,**kwargs)
        self.count_of_pages = 0



    def parse(self, response):
        pass
