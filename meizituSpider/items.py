# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class mwizituspiderItem(scrapy.Item):

    link = scrapy.Field() # 链接
    name = scrapy.Field() # 主题
    tag = scrapy.Field() # 标签
    time = scrapy.Field() # 拍照时间
    createtime = scrapy.Field() # 爬取时间
    code = scrapy.Field() # 二进制
