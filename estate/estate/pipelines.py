# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
import pymysql

class EstatePipeline:
    connect = pymysql.connect(host="localhost", port=3306, user="root", passwd="root", db="room", charset="utf8")
    def process_item(self, item, spider):
        sql = "insert into rooms values(%s,%s,%s,%s,%s,%s,%s)"
        cursor = self.connect.cursor()
        cursor.execute(sql, (item['job_title'], item['job_way'], item['job_house'], item['job_area'], item['job_orientation'], item['job_address'], item['job_price']))
        self.connect.commit()
        return item
