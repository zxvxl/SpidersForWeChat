# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import logging
import sys
import scrapy
import subprocess
from scrapy.http import HtmlResponse
from selenium import webdriver
from scrapy.selector import Selector
from ..items import ArticleItem
import pytesseract
from PIL import Image
from .. import fetch_free_proxyes
type = sys.getfilesystemencoding()
reload(sys)
sys.setdefaultencoding('utf-8')

logger = logging.getLogger("test spider")

class TestSpider(scrapy.Spider):
    name = "test"
    #allowed_domains = ["103.243.24.223"]
    website_possible_httpstatus_list = [403]
    handle_httpstatus_list = [403]
    
    start_urls = [
        "http://weixin.sogou.com/weixin?query=大数据文摘",
        "http://weixin.sogou.com/weixin?query=开源中国",
        "http://weixin.sogou.com/weixin?query=码农翻身",
    ]

    def parse(self, response):
        if response.body == "banned":
            req = response.request
            req.meta["change_proxy"] = True
            yield req
        else:
            history_page_url = response.xpath('//li[@id="sogou_vr_11002301_box_0"]/div[@class="gzh-box2"]/div[@class="img-box"]/a/@href').extract()[0]
            cmd = 'phantomjs E:\phantomjs\/bin\getBody.js "%s"' % history_page_url
            stdout, stderr = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE).communicate()
            stdout = stdout.replace('\r\n', '')
            response = HtmlResponse(url=history_page_url, body=stdout)
            articleList = []
            items = []
            wxInfo = Selector(text=response.body).xpath(
                '//div[@class="profile_info_area"]/div[@class="profile_info_group"]/div[@class="profile_info"]')
            wxName = wxInfo[0].xpath('strong[@class="profile_nickname"]/text()').extract()[0].encode('utf-8')
            wxCode = wxInfo[0].xpath('p[@class="profile_account"]/text()').extract()[0].encode('utf-8')
            articleList = Selector(text=response.body).xpath(
                '//div[@id="history"]/div[1]/div[2]/div[@class="weui_media_box appmsg"]/div[@class="weui_media_bd"]')
            wx_domain = "https://mp.weixin.qq.com"
            wx_domain = wx_domain.decode(type).encode('utf-8')
            if len(articleList) == 0:
                req = response.request
                req.meta["change_proxy"] = True
                yield req
            else:
                for i in range(len(articleList)):
                    item = ArticleItem()
                    item['wxName'] = wxName.strip()
                    item['wxCode'] = wxCode.strip()
                    hrefs = wx_domain + articleList.xpath('h4/@hrefs').extract()[i].encode('utf-8')
                    desc = articleList.xpath('//*[contains(@class, "weui_media_desc")]/text()').extract()[i].encode(
                        'utf-8')
                    pubtime = articleList.xpath('//*[contains(@class, "weui_media_extra_info")]/text()').extract()[
                        i].encode('utf-8')
                    item['hrefs'] = hrefs.strip()
                    item['desc'] = desc.strip()
                    item['pubtime'] = pubtime.strip()
                    items.append(item)

                for item in items:
                    #self.article_content(item)
                    yield scrapy.Request(item['hrefs'], meta={'item': item},callback=self.article_content)  # 循环获取每篇文章内容

    def article_content(self, response):
        item = response.meta['item']
        title = Selector(text=response.body).xpath('//h2[@id="activity-name"]/text()').extract()[0].encode(
            'utf-8').strip()
        content = Selector(text=response.body).xpath('//*[@id="js_article"]/div[@class="rich_media_inner"]').extract()[
            0].encode('utf-8')
        content = content.replace('\r\n', '').strip()
        item['title'] = title
        item['content'] = content
        return item  # 返回item，执行数据库操作