# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

#BolePipeline：自定义的！

class BolePipeline(object):

    def __init__(self):
        self.db = None
        self.cursor = None

    def process_item(self, item, spider):

        self.db = pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='root',
            db='meizitu'
        )

        self.cursor = self.db.cursor()
        data = {
                    "link":item['link'],
                    "name":item['name'],
                    "tag":item['tag'],
                    "time":item['time'],
                    "createtime":item['createtime'],
                    "code":item['code'],
                }

        insert_sql = "INSERT INTO meizitu (link,name,tag,time,createtime,code) VALUES (%s,%s,%s,%s,%s,%s)"

        try:

            self.cursor.execute(
                insert_sql,
                (
                    data['link'],
                    data['name'],
                    data['tag'],
                    data['time'],
                    data['createtime'],
                    data['code']
                )
            )

            self.db.commit()

        except Exception as e:
            print('问题数据跳过！.......', e)
            self.db.rollback()
        self.cursor.close()
        self.db.close()
        return item

