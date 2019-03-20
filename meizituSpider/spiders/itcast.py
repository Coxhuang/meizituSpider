# -*- coding: utf-8 -*-
import scrapy
from meizituSpider.items import mwizituspiderItem
from datetime import datetime

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['mzitu.com']
    start_urls = (
        'https://www.mzitu.com/jiepai/comment-page-1/',
    )

    def parse(self, response):

        for page in range(1,20):

            url_next = "https://www.mzitu.com/jiepai/comment-page-{}/".format(page)

            yield scrapy.Request(url_next, callback=self.parse_response_next)


    def parse_response_next(self,response):

        meizitu_item = mwizituspiderItem()
        now = datetime.now()

        for img_response in response.xpath('/html/body/div[2]/div[1]/div[2]/div/ul/li'):

            img_url = img_response.xpath('div/p/img/@data-original').extract_first()
            img_time = img_response.xpath('normalize-space(div/div[2]/a/text())').extract_first()

            meizitu_item["link"] = img_url
            meizitu_item["name"] = "街拍"
            meizitu_item["tag"] = "街拍"
            meizitu_item["time"] = img_time
            meizitu_item["createtime"] = now
            meizitu_item["code"] = ""

            yield meizitu_item
