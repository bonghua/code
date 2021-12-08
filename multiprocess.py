from multiprocessing import Manager,Pool
import multiprocessing,requests,csv
from fake_useragent import UserAgent

file=open('multi3.csv','w',newline='')
writer=csv.writer(file)
writer.writerow(['概要','来源','发布时间','标题','网址'])

def ur(q):
    for i in range(5):
        urll='https://assets.msn.cn/service/news/feed/pages/wpoxfeed?InterestIds=Y_82678d1b-b69e-4790-b964-8f2f7b0b3827&User=m-21B80B24F9CD641A2DA404B2F88E6544&activityId=B7F6B308-19BB-492D-B0F0-B64A3A6E63AB&apikey=0QfOX3Vn51YCzitbLaRkTTBadtWpgTN8NZLW0C1SEM&audienceMode=adult&cardsServed=52&contentType=article,video,slideshow,webcontent&fdhead=msnallexpusers,muidflt12cf,muidflt13cf,muidflt16cf,muidflt27cf,1s-cuseraip,muidflt57cf,oneboxdhpcf,mmxandroid1cf,audexedge3cf,moneyedge3cf,pnehp2cf,pnehp3cf,starthp2cf,moneyhp1cf,bingcollabhz1cf,artgly5cf,article4cf,gallery2cf,1s-bing-news,vebudumu04302020,bbh20200521msncf,prg-1sw-spvdn,prg-vbkgd1-2c,prg-mapspivot,prg-1sw-crnr4,prg-1sw-revtr,preprg-1sw-nc5,prg-1sw-adctrl,prg-1sw-recfvc,prg-ts-toprr,msnsapphire2cf,1s-remotecompact,prg-adspeek,edgpowert,prg-entsc-t,csmoney7cf,1s-br30min,1s-br30mincn,1s-winauthservice,5b2a7679,prg-1sw-n-api1,1s-winsegservice,prg-1sw-delayfeed10,prg-1sw-reloadshell,prg-1sw-falt,prg-wf-sky-re,msnapp6cf,prong2c,1s-pagesegservice,prg-1sw-ms-cloudc,prg-1sw-mscloudn,routentpring2c,prg-1s-p2pre,prg-suggestionwc,prg-sh-tabgg,8912i356,prg-wpo-infhent&market=zh-cn&newsSkip='+str(46+50*i)+'&newsTop=48&ocid=anaheim-ntp-feeds&rid=b7f6b30819bb492db0f0b64a3a6e63ab&timeOut=3000&wpoCmsAdServed=4&wpoNativeAdServed=6'
        q.put_nowait(urll)
        
def pars(q):
    while not q.empty():
        url=q.get_nowait()
        
        user=UserAgent(path=r'../py资料/爬虫/UserAgent.json').random
        headers={'UserAgent':str(user)}
        response=requests.get(url,headers=headers)
        
        dat=response.json()
        
        data=dat['sections']
        for i in data:
            data2=i['cards']
            for pi in data2:
                try:
                    abstract=pi['abstract']
                    provider=pi['provider']['name']
                    publish_time=pi['publishedDateTime']
                    title=pi['title']
                    urll=pi['url']
                    writer.writerow([abstract,provider,publish_time,title,urll])
                    
                    print(abstract)
                except:
                    print(pi)
                
if __name__=='__main__':
    q=Manager().Queue()
    pool=Pool(multiprocessing.cpu_count())
    pool.apply_async(func=ur,args=(q,))
    for i in range(20):
        pool.apply_async(func=pars,args=(q,))
    pool.close()
    pool.join()
    
    file.close()
    