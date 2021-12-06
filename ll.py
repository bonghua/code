from gevent import monkey
monkey.patch_all()
from gevent.queue import Queue
import gevent,re,requests,csv,time
from bs4 import BeautifulSoup
from selenium import webdriver
import uuid,random

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52'
,'Referer':'https://js.wotucdn.com/!!framework/web/public/mainsite/css/reset-style.css,framework/public/common/css/refresh_css_so.v4.11.56.css,framework/web/weili/new-list/css/font/iconfont.css,framework/web/public/mainsite/css/font/iconfont.css,framework/web/public/mainsite/css/wt-public.css,framework/web/weili/new-list/css/wt-list.css?v=202107271437'}
for s in range(0,3):
    response=requests.get('https://cn.bing.com/images/search?q=%e7%be%8e%e5%9b%be%e7%bd%91&form=HDRSC2&first='+str(s)+'&tsc=ImageBasicHover',headers=headers)
    data1=BeautifulSoup(response.text,'html.parser')
    queue=Queue()
    data2=data1.find_all(class_='mimg vimgld')
    data22=data1.find_all(class_='mimg')

    for a in data2:
            path=a['data-src']
            uu=re.search('.*-(\w.*H)?.*',path)
            queue.put_nowait(path)
    for k in data22:
            print(k)
            try:
                path2=k['data-src']
            except:
                path2=k['src']
            queue.put_nowait(path2)
    
    '''name=uu.group(1)  
    us=re.sub('C.','k',str(name))
    ub=Queue()'''



def cr():
    while not queue.empty():
        ur=queue.get_nowait()
        response2=requests.get(ur)  
        ll=1
        ll+=1
        s=random.randint(0,10000)
        with open(f'./stor/{s}.jpg','wb') as im:
            im.write(response2.content)
            im.close()    
  
lists=[]
for i in range(0,3):
    list=gevent.spawn(cr)
    lists.append(list)
gevent.joinall(lists)
