from typing import Iterable, Any
from pathlib import Path
import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy import Request
from scrapy.http import Response


class GameCrawlerSpider(scrapy.Spider):
    name = "game_crawler"
    allowed_domains = ["en.wikipedia.org"]
    custom_settings = {
        'DEPTH_LIMIT': 3,
        'MAX_PAGES': 300
    }



    def __init__(self, *args, **kwargs):
        super(GameCrawlerSpider, self).__init__(*args, **kwargs)
        self.count_of_pages = 0

    def start_requests(self):
        start_urls = ["https://en.wikipedia.org/wiki/Video_game"]
        yield from (scrapy.Request(url=url, callback=self.parse) for url in start_urls)

    def parse(self, response):
        if self.count_of_pages >= self.custom_settings.get('MAX_PAGES'):
            self.logger.info(f"Maximum Limit has been reached ({self.custom_settings.get('MAX_PAGES')})")
            return
        content = response.css("div.mw-content-ltr")
        page_name = response.url.split("/")[-1]
        folder = "C:\Illinois Tech\Sem 2\Information Retrival\Video_Game_Crawler\Video_Game_Crawler\webpages"
        file_name = f"Gamepage-{page_name}.html"
        file_location = Path(f'{folder}/{file_name}')
        file_location.write_bytes(response.body)

        self.count_of_pages += 1
        yield {
            # "content": "".join(list(filter(lambda x : x != "\n", details.css("div.mw-content-ltr p::text").getall()))),
            "title": response.css("span.mw-page-title-main::text").get(),
            "content": "".join(content.css("p::text").getall()).replace("\n", ""),
            "link": response.url,
            "filename": file_name
        }
        for link in response.css("div.mw-content-ltr p a::attr(href)").extract()[:10]:
            if link.startswith("/wiki/") and ':' not in link:
                yield response.follow(link, callback=self.parse)



