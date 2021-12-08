from multiprocessing import Manager,Pool,Queue
import multiprocessing,requests,csv
from fake_useragent import UserAgent

file=open('multi.csv','w',newline='',encoding='utf-8')
writer=csv.writer(file)

def urr(q):
        for i in range(50):            
            urlk='https://3g.163.com/fe/api/hot/news/combine?pageNo='+str(i)+'&pageSize=15'
            q.put_nowait(urlk)
            
def parse(q):
    while not q.empty():
        url=q.get_nowait()
        user=UserAgent(path=r'../py资料/爬虫/UserAgent.json').random
        headers={'UserAgent':str(user)}
        response=requests.get(url,headers=headers)
        response2=response.json()
        data=response2['data']['list']
        for a in data:
            print(a['title'])
            title=a['title']
            time=a['createTime']
            publishtime=a['publishTime']
            source=a['source']
            writer.writerow([title,time,publishtime,source])
               
if __name__=='__main__':
    q=Manager().Queue()
    pool=Pool(multiprocessing.cpu_count())
    pool.apply_async(func=urr,args=(q,))
    for i in range(10):
        pool.apply_async(func=parse,args=(q,))
    pool.close()
    pool.join()
    
    file.close()
    
    