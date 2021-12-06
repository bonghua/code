
from ..items import GoItem
import scrapy
from  bs4 import BeautifulSoup
class spp(scrapy.Spider):
    name='go'
    allow_domains='chinapolicy.com'
    start_urls=['http://www.chinapolicy.com.cn/']
    def parse(self,response):
        data1=BeautifulSoup(response.text,'html.parser')
        data2=data1.find(class_='container4')
        data3=data2.find_all('span')
        for i in data3:
            data4=i.find('a')
            url=data4['href']
            path='http://www.chinapolicy.com.cn/'+url
            yield scrapy.Request(path,callback=self.she)
    def she(self,response):
        da1=BeautifulSoup(response.text,'html.parser')
        da2=da1.find_all('a')
        #da3=da2.find_all('a')
        itt=GoItem()
        for a in da2:
            dd=a.text
            itt['tex']=dd
            yield itt
            