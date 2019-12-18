#전체 또는 지역구들의 변동률을 구하기 위한 코드

import urllib.request
import pandas as pd
import datetime
from itertools import count
import time
from selenium import webdriver
import ssl  #추가


def getValue(result):
    wd = webdriver.Chrome('C:/Python36/chromedriver_win32/chromedriver.exe')
    url = 'https://www.r-one.co.kr/rone/resis/statistics/statisticsViewer.do?menuId=HOUSE_21111'

    wd.get(url)
    time.sleep(1)
    wd.implicitly_wait(5)

    
    #아파트 클릭_ 하지않으면 주택가격이 크롤링됨! 주의
    wd.find_element_by_xpath("""//*[@id="HOUSE_21200"]/a""").click()
    wd.implicitly_wait(5)
    time.sleep(1)

    #매매가격지수 클릭
    wd.find_element_by_xpath("""//*[@id="HOUSE_21210"]/a""").click()
    wd.implicitly_wait(5)
    time.sleep(1)
    wd.find_element_by_xpath("""//*[@id="HOUSE_21211"]/a""").click()
    wd.implicitly_wait(12)
    time.sleep(1)
    
    wd.find_element_by_xpath("""//*[@id="srchType"]/option[text()='전체']""").click()
    wd.implicitly_wait(5)
    time.sleep(1)


    #상세지역 선택 버튼 클릭 / 상세 지역 선택할 시
    #wd.find_element_by_xpath("""/html/body/div[2]/div[1]/div[2]/div/div[1]/div/ul/li[3]/img""").click()
    #wd.implicitly_wait(5)
    #time.sleep(1)
    
    #검색기간 년도 선택 (2006년) 
    wd.find_element_by_xpath("""//*[@id="researchYear_s"]/option[text()='2006년']""").click()
    wd.implicitly_wait(5)
    time.sleep(1)

    #검색기간 월 선택 (11월)
    wd.find_element_by_xpath("""//*[@id="researchMonth_s"]/option[text()='02월']""").click()
    wd.implicitly_wait(5)
    time.sleep(1)

    #검색종료기간 년도 선택(2019년)
    wd.find_element_by_xpath("""//*[@id="researchYear_e"]/option[text()='2019년']""").click()
    wd.implicitly_wait(5)
    time.sleep(1)

    #검색종료기간 월 선택(11월)
    wd.find_element_by_xpath("""//*[@id="researchMonth_e"]/option[text()='11월']""").click()
    wd.implicitly_wait(5)
    time.sleep(1)

    #확인 클릭
    wd.find_element_by_xpath("""//*[@id="statisticsBtnOk"]""").click()
    wd.implicitly_wait(25)
    time.sleep(10)

    for i in range(1,2):
        #city는 딱 두번만 바뀌므로 큰 for문에 넣는다.
        num = str(i+1)
        print(f"""//*[@id="tableStyle"]/tbody/tr[{num}]/td[1]""")
        city = wd.find_element_by_xpath(f"""//*[@id="tableStyle"]/tbody/tr[{num}]/td[1]""").text
                                 
        print(city)
        #날짜가 5개 이후부터 크롤링이 안돼서 불가피하게 코딩으로 처리
        date = wd.find_element_by_xpath(f"""/html/body/div[1]/div[2]/div/div/div[1]/div[3]/div/div[2]/div/table/thead/tr[1]/th[2]""").text.replace("'",'').split('.')
        date[0] = int(date[0])
        date[1] = int(date[1])
        print(date)
        for idx in count():
            try:
                #date와 value는 수시로 바뀌므로 작은 for문에 넣는다.
                #date = wd.find_element_by_xpath("""//*[@id="tableStyle"]/thead/tr[1]/th["""+(str(idx+2))+"""]""").text()
                #date = wd.find_element_by_xpath(f"""//*[@id="tableStyle"]/thead/tr[1]/th[{str(idx+2)}]""").text
                
                #year
                if(idx != 0):
                    date[1] = date[1]+1
                    if(date[1] == 13):
                        date[0] = date[0]+1
                        date[1] = 1
                print(date)
                # tbody > tr[0] > td중에 2,4,6,8가져오면 됨.
                #value의 td태그 변동률은 짝수 단위로 가져와야 하므로 (str(2*(idx+1)+1))
                #value = wd.find_element_by_xpath(f"""//*[@id="tableStyle"]/tbody/tr[1]/td[{str(2*(idx+1)+1)}]""").text
                value = wd.find_element_by_xpath(f"""/html/body/div[1]/div[2]/div/div/div[1]/div[3]/div/div[4]/table/tbody/tr[{num}]/td[{str(2*(idx)+6)}]""").text
 
                print(value)                       
                # 2004 or 2019를 만들기 위해 
                if(len(str(date[0])) == 1):
                    year_month = '200'+str(date[0])+" "+str(date[1])
                else:
                    year_month = '20'+str(date[0])+" "+str(date[1])
                
                #year_month = str(date[0])+'.'+str(date[1])
                result.append([city]+ [year_month]+ [value])
            except Exception as e:
                print(e)
                break
    return

def csv_value():
    
    result = []
    print('변동률을 크롤링합니다.')
    
    getValue(result)
    csv_table = pd.DataFrame(result, columns=('city', 'date', 'value'))
    csv_table.to_csv("수도권_변동률.csv", encoding="cp949", mode='w', index=True)
    
    del result[:]
    print('FINISHED')
    
if __name__ == '__main__':
    csv_value()
