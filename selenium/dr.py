from gevent import monkey
monkey.patch_all()
import gevent,csv,time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
from gevent.queue import Queue
# 引入活动链 和 按键类
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

fil=open('neiyi2.csv','w',newline='')
file=csv.writer(fil)

# 使用滚轮不可隐式爬取
'''option=Options()
option.add_argument('--headless')'''



queue=Queue()
for i in range(50):
    ur='https://search.suning.com/%E5%86%85%E8%A1%A3/&iy=0&isNoResult=0&cp='+str(i)+'#second-filter'
    queue.put_nowait(ur)
def nei():
    while not queue.empty():
        url=queue.get_nowait()
# 每次在同一网页异步登入网址，会出现执行过快 滚轮来不及动的情况，因此一个网站一个浏览器
        driver=webdriver.Chrome()
        driver.get(url)
        time.sleep(2)
# 活动链：执行 滚轮滚动到最底端脚本，通过按下“向下键”
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        ActionChains(driver).key_down(Keys.DOWN).perform()
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
        driver.close()
list=[]
for i in range(10):
    ass=gevent.spawn(nei)
    list.append(ass)
gevent.joinall(list)

fil.close()
        