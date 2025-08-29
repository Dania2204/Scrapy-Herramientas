import scrapy
import time


class WorldSpider(scrapy.Spider):
    name = "world"
    start_urls = [
        "https://worldmetrics.org/upskilling-and-reskilling-in-the-steel-industry-statistics/"
    ]

    def parse(self, response):

        stats = response.css("ul li p::text").getall()

        stats = [s.strip() for s in stats if s.strip()]

        yield {
            "ai_waste_statistics": "\n".join(stats),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        }
