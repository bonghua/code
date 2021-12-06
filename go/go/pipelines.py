# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl

class GoPipeline:
    def __init__(self) :
        self.wb=openpyxl.Workbook()
        self.ws=self.wb.active

        
    def process_item(self, item, spider):
        data=[item['tex']]
        self.ws.append(data)
        return item
    def close_spider(self,spider):
        self.wb.save('hh.xlsx')
        self.wb.close()
