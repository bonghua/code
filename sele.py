from gevent import monkey
monkey.patch_all()
from gevent.queue import Queue
import requests,time,gevent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# 静默模式设置
opti=Options()
opti.add_argument('--headless')
driver=webdriver.Chrome(options=opti)
# 隐式等待
driver.implicitly_wait(5)
# 有关于2次登录（破反爬）的函数封装
def sel():
    driver.get('')
    
    un=driver.find_element_by_id('un')
    un.send_keys('')
    
    pd=driver.find_element_by_id('pd')
    pd.send_keys('')
    
    botton=driver.find_element_by_class_name('login_box_landing_btn')
    botton.click()
    
    xj=driver.find_element_by_name('USERNAME')
#xh=driver.find_element_by_id('xh')
    xj.send_keys('')
    
    pwd=driver.find_element_by_id('pwd')
    pwd.send_keys('')
    
    bo=driver.find_element_by_id('btnSubmit')
    bo.click()
# 最重要重点：selenium同一浏览器登陆后，携带cookies，直接访问里面信息的网址，不用再登陆，可直接访问
# 信息异步爬取函数封装
def pa():
    url=['','','','']
    queue=Queue()
    for i in url:
        queue.put_nowait(i)
        
    def hh():
        while not queue.empty():
            ur=queue.get_nowait()
            driver.get(ur)
            data=driver.find_element_by_class_name('Nsb_layout_r')
            print(data.text)
    list=[]
    for i in range(3):
        ass=gevent.spawn(hh)
        list.append(ass)

    gevent.joinall(list)
# 2个函数的调用
sel()
pa()
