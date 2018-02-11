# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleItem(scrapy.Item):
    wxName = scrapy.Field()
    wxCode = scrapy.Field()
    title = scrapy.Field()
    hrefs = scrapy.Field()
    desc = scrapy.Field()
    pubtime = scrapy.Field()
    content = scrapy.Field()
