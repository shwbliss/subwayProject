#호갱노노 사이트 아파트별 크롤링 
import urllib.request
import pandas as pd
import datetime
from itertools import count
import time
from selenium import webdriver
#호갱노노 사이트는 .click 함수가 실행되지않아 keys를 사용해야함 
from selenium.webdriver.common.keys import Keys
from itertools import count

def getApartment(url, result):
    
    #검색 아파트
    #search_apart = ''
    wd = webdriver.Chrome('C:/Python36/chromedriver_win32/chromedriver.exe')
    
    wd.get(url)
    wd.implicitly_wait(10)
    time.sleep(1)
    
    
    #회원 로그인
    wd.find_element_by_xpath("""//*[@id="container"]/div[3]/a""").send_keys(Keys.ENTER)
    wd.find_element_by_name("username").send_keys('01063955862')
    wd.find_element_by_name("password").send_keys('446602')
    #클릭
    wd.find_element_by_xpath("""/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]/a[1]""").send_keys(Keys.ENTER)
    wd.implicitly_wait(10)
    time.sleep(1)
    
    wd.find_element_by_xpath("""/html/body/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/div[1]/a[2]""").send_keys(Keys.ENTER)
    wd.implicitly_wait(5)
    time.sleep(1)
    
    #wd.find_element_by_xpath("""/html/body/div[2]/div/div[1]/div[2]/a""").send_keys(Keys.ENTER)
   # wd.implicitly_wait(5)
    #time.sleep(1)
    
    #검색창에 아파트 입력
    #wd.find_element_by_xpath("""/html/body/div[2]/div/div[1]/div[1]/div[3]/div/div[4]/div/div/fieldset/div[1]/div/input""").send_keys(search_apart)
    #wd.implicitly_wait(10)
    #time.sleep(1)
    
    #실거래가 스크롤 끝까지 내리기 //아파트별로 차이가 크기 때문에 count()사용
    for idx in count():        
        try:
            wd.find_element_by_xpath("""/html/body/div[2]/div/div[1]/div[1]/div[3]/div/div[4]/div/div/div/div[1]/div[3]/div[3]/div[3]/a""").send_keys(Keys.ENTER)
        except:
            break
    table = wd.find_element_by_xpath("""/html/body/div[2]/div/div[1]/div[1]/div[3]/div/div[4]/div/div/div/div[1]/div[3]/div[3]/div[3]/table""")
    trs = table.find_elements_by_css_selector('tr')
    for i in count():
        try:
            tds = trs[i].find_elements_by_css_selector('td')
            result.append([tds[0].text] + [tds[1].text] + [tds[2].text])
        except:
            break
     
def csv_value():
    
    result = []
    print('아파트 실거래가를 크롤링합니다.')

    #사이트 url
    url = "https://hogangnono.com/apt/1tm03/0/4"

    #크롤링함수 호출
    getApartment(url, result)
    
    csv_table = pd.DataFrame(result, columns=('date', 'value', 'size'))
    
    #평수가 다양하므로 이어 저장해야 한다
    #따라서 header부분은 또 입력하지 않기 때문에 false
    #index는 이어져야 하므로 true 설정 
    csv_table.to_csv("아파트/명수대현대.csv", encoding="cp949", mode='a',header=False, index=True)
    
    del result[:]
    print('FINISHED')
    
if __name__ == '__main__':
    csv_value()
