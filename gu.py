import fake_useragent
from gevent import monkey
from gevent import queue
monkey.patch_all()
from gevent.queue import Queue
import requests,re,json,gevent,sqlite3
from fake_useragent import UserAgent
connect=sqlite3.connect('D:/demm.db')
cursor=connect.cursor()
#cursor.execute('''CREATE TABLE tnll(序号 integer primary key AUTOINCREMENT,新闻标题 text)''')
queue=Queue()
for i in range(2,5):
    ur='https://sports.cctv.com/2019/07/gaiban/cmsdatainterface/page/remen_'+str(i)+'.jsonp?cb=remen'
    queue.put_nowait(ur)
def success():
    while not queue.empty():
        user=UserAgent(path=r'../py资料/爬虫/UserAgent.json').random
        headers={'UserAgent':str(user)}
        url=queue.get_nowait()
        response=requests.get(url,headers=headers)
        response.encoding='utf-8'
        '''ress=re.findall('remen(.*)',response.text)
#print(len(ress[0])) 
        a=json.loads(ress[0][1:len(ress[0])+1])'''
        ress=response.text[6:len(response.text)-1]
        
        a=json.loads(ress)
        #print(ress)
        data=a['data']['list']
        for i in data:
            print(i['title'])
            #data2=i['title']
            #cursor.execute(f"INSERT INTO  tnll(新闻标题) VALUES('{data2}')")
            #connect.commit()
list=[]
for i in range(5):
    assign=gevent.spawn(success)
    list.append(assign)
gevent.joinall(list)
connect.close()



