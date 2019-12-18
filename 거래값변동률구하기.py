#평균값들을 이용해 변동률 구하기

import pandas

def getValue(res):
    df = pandas.read_csv('아파트\신분당선avg.csv', encoding='cp949')

    for i in range(0, (df.shape[0]-1)):
        if(df['average'][i] != 0 and df['average'][i+1] != 0):
            print('===%s' %(df['date'][i+1]))
            value = round((df['average'][i+1] - df['average'][i])/df['average'][i],2)
            print(value)
            date = df['date'][i+1]
            res.append([date] + [value])
        else:
            value = 0
            date = df['date'][i+1]
            res.append([date] + [value])


def csv_value():
    
    res = []
    print('변동률을 계산합니다.')

    #함수 호출
    getValue(res)
    
    csv_table = pandas.DataFrame(res, columns=('date', 'value'))
    
    csv_table.to_csv("아파트/신분당선result.csv", encoding="cp949", mode='w', index=True)
    
    del res[:]
    print('FINISHED')
    
if __name__ == '__main__':
    csv_value()   
