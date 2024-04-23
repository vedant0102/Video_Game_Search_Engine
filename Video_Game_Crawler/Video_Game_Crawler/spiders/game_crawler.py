from typing import Iterable, Any
from pathlib import Path
import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy import Request
from scrapy.http import Response


class GameCrawlerSpider(scrapy.Spider):
    # Name of the spider
    name = "game_crawler"
    # Allowed domains to crawl
    allowed_domains = ["en.wikipedia.org"]
    # Custom settings for the spider
    custom_settings = {
        'DEPTH_LIMIT': 4,  # Limit the depth of crawling
        'MAX_PAGES': 500,  # Maximum number of pages to crawl
        # If you want to do crawl concurrently, uncomment the following line
        #'CONCURRENT_REQUESTS': 8
    }

    def __init__(self, *args, **kwargs):
        # Initialize the spider
        super(GameCrawlerSpider, self).__init__(*args, **kwargs)
        # Counter to keep track of the number of crawled pages
        self.count_of_pages = 0

    def start_requests(self):
        # Start crawling from these URLs
        start_urls = ["https://en.wikipedia.org/wiki/Video_game"]
        # Generate requests for each URL
        yield from (scrapy.Request(url=url, callback=self.parse) for url in start_urls)

    def parse(self, response):
        # Check if maximum page limit has been reached
        if self.count_of_pages >= self.custom_settings.get('MAX_PAGES'):
            # Log a message indicating that the maximum limit has been reached
            self.logger.info(f"Maximum Limit has been reached ({self.custom_settings.get('MAX_PAGES')})")
            return
        # Extract content from the response
        content = response.css("div.mw-content-ltr")
        # Get the page name from the URL
        page_name = response.url.split("/")[-1]
        # Define folder and file paths to save the webpages
        folder = "C:\Illinois Tech\Sem 2\Information Retrival\Video_Game_Crawler\Video_Game_Crawler\webpages"
        file_name = f"Gamepage-{page_name}.html"
        file_location = Path(f'{folder}/{file_name}')
        # Save the webpage as HTML file
        file_location.write_bytes(response.body)

        # Increment the page counter
        self.count_of_pages += 1
        # Yield information about the crawled page
        yield {
            "title": response.css("span.mw-page-title-main::text").get(),
            "content": "".join(content.css("p::text").getall()).replace("\n", ""),
            "link": response.url,
            "filename": file_name
        }
        # Extract links from the response and follow them for further crawling
        for link in response.css("div.mw-content-ltr p a::attr(href)").extract()[:10]:
            # Check if the link is a Wikipedia article and not a special page
            if link.startswith("/wiki/") and ':' not in link:
                # Follow the link and call the parse method recursively
                yield response.follow(link, callback=self.parse)
