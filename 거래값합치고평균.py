#크롤링한 데이터들을 합치고 평균을 내서 다시 csv로 저
import pandas
import urllib.request


def getAverage(res):
    df = pandas.read_csv('아파트\신분당선.csv', encoding='cp949')



        
    #print(df['가격'][i])
    result = {}
    count = {}
    for i in range(1,13):
        result[i] = 0
    for i in range(1,13):
        count[i] = 0

    for j in range(2006, 2020):       
        for i in range(0, df.shape[0]):
            date = df['계약일'][i].split('.')
            if(date[0] == str(j)):
                for k in range(1, 13):
                    if(int(date[1]) == k):
                        result[k] = result[k]+int(df['가격'][i])
                        count[k] = count[k] + int('1')
        print(count)
        for i in range(1, 13):
            if(count[i] != 0):
                result[i] = result[i]//count[i]
            new_date = str(j)+' '+str(i)
            res.append([new_date] + [result[i]])
        print(f"%s년===" %j, result)
        for i in range(1,13):
            result[i] = 0
        for i in range(1,13):
            count[i] = 0
                            
def csv_sum_value():
    
    res = []
    print('평균을 계산합니다.')

    #함수 호출
    getAverage(res)
    
    csv_table = pandas.DataFrame(res, columns=('date', 'average'))
    
    csv_table.to_csv("아파트/신분당선avg.csv", encoding="cp949", mode='w', index=True)
    
    del res[:]
    print('FINISHED')
    
if __name__ == '__main__':
    csv_sum_value()          


