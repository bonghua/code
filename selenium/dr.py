from gevent import monkey
monkey.patch_all()
import gevent
from selenium.webdriver.chrome .options import Options
from selenium import webdriver
import csv,time
from bs4 import BeautifulSoup
from gevent.queue import Queue

fil=open('neiyi2.csv','w',newline='')
file=csv.writer(fil)

option=Options()
option.add_argument('--headless')
driver=webdriver.Chrome(options=option)


queue=Queue()
for i in range(50):
    ur='https://search.suning.com/%E5%86%85%E8%A1%A3/&iy=0&isNoResult=0&cp='+str(i)+'#second-filter'
    queue.put_nowait(ur)
def nei():
    while not queue.empty():
        url=queue.get_nowait()

        driver.get(url)
        time.sleep(3)
        source=driver.page_source
        text=BeautifulSoup(source,'html.parser')
        selling=text.find_all(class_='title-selling-point')
        for i in selling:
            com=i.find('a')
            #ura=com['url']
            title=com.text
            print(title)
            file.writerow([title])
list=[]
for i in range(10):
    ass=gevent.spawn(nei)
    list.append(ass)
gevent.joinall(list)

fil.close()
         
