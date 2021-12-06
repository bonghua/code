from gevent import monkey
from gevent import queue
monkey.patch_all()
from gevent.queue import Queue
import gevent
import requests,csv
from bs4 import BeautifulSoup
import re

file=open('ss.csv','w',encoding='utf-8',newline='')
writer=csv.writer(file)
que=Queue()
for i in range(1):
    ur=input('请输入你想要搜索的词条')
    path='https://baike.baidu.com/item/'+ur
    que.put_nowait(path)
def cra():
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84',
'Refer':'https://cn.bing.com/'}
    while  not que.empty():
        url=que.get_nowait()
        response=requests.get(url,headers=headers)
#response.encoding='gbk'
        print(response.status_code)
        data=BeautifulSoup(response.text,'html.parser')
        dataa=data.find(class_='basic-info J-basic-info cmn-clearfix')
        name=dataa.find_all('dt',class_='basicInfo-item name')
        value=data.find_all(class_='basicInfo-item value')
        for i in range(len(name)):
            data1=re.findall('\w+',name[i].text)
            #if data1==[]:
                #continue
            data2=re.findall('\w+',name[i].text)
            writer.writerow([data1,data2])
            print(data1,data2)
lis=[]
for i in range(3):
    ass=gevent.spawn(cra)
    lis.append(ass)
gevent.joinall(lis)    
file.close()



    


