from sqlite3.dbapi2 import Cursor, connect
from gevent import monkey
monkey.patch_all()
from gevent.queue import Queue
import sqlite3,gevent,requests
from fake_useragent import UserAgent
connect=sqlite3.connect('D:/demm.db')
cursor=connect.cursor()
cursor.execute('CREATE TABLE gitnew9(序号 INTEGER primary key AUTOINCREMENT,新闻标题 TEXT,创造时间 TEXT,发布时间 TEXT,数据来源 TEXT)')
queue=Queue()
for i in range(50):
    url='https://3g.163.com/fe/api/hot/news/combine?pageNo='+str(i)+'&pageSize=15'
    queue.put_nowait(url)
def gi():
    while not queue.empty():
        user=UserAgent(path=r'C:\Users\奉华\Desktop\py资料\爬虫\UserAgent.json').random
        headers={'UserAgent':str(user)}
        ur=queue.get_nowait()
        respon=requests.get(ur,headers=headers)
        response=respon.json()
        data=response['data']['list']
        for a in data:
            print(a['title'])
            title=a['title']
            time=a['createTime']
            publishtime=a['publishTime']
            source=a['source']
            
            cursor.execute(f"INSERT INTO gitnew9(新闻标题,创造时间,发布时间,数据来源) VALUES('{title}','{time}','{publishtime}','{source}')")
            
                
            connect.commit()
list=[]
for i in range(5):
    assign=gevent.spawn(gi)
    list.append(assign)
gevent.joinall(list)
            
        
        
        