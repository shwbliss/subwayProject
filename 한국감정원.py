#한국감정원 사이트 크롤링 but 태그가 읽혀오지 않
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import datetime
from itertools import count
import ssl  #추가
def get_request_url(url, enc='utf-8'):
    
    req = urllib.request.Request(url)

    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            try:
                rcv = response.read()
                ret = rcv.decode(enc)
            except UnicodeDecodeError:
                ret = rcv.decode(enc, 'replace')                
            return ret
            
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None
def getValue():   
  
    URL = 'http://www.kab.co.kr/kab/home/trend/market_trend02.jsp'
    print (URL)

    try:
        rcv_data = get_request_url(URL)
        #print('1')
        soupData = BeautifulSoup(rcv_data, 'html.parser')
        tbody= soupData.find('tbody', attrs={ 'id':'listStat'})
        print(tbody)

    except Exception as e:
        print(e)
        return
def cswin_Chuga ():
    print('한국감정원 CRAWLING START')
    getValue()
    
if __name__ == '__main__':
     cswin_Chuga ()
