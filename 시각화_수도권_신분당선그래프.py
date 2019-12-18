#수도권-신분당선 그래프
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager, rc
from pandas import DataFrame
import numpy
from itertools import count

def getYear(start, finish, year):
    start_n = start.split('/')
    start_n[0] = int(start_n[0])
    start_n[1] = int(start_n[1])
    for idx in count():
        start_n[1] = start_n[1] + 1
        if(start_n[1] == 13):
            start_n[0] = start_n[0] + 1
            start_n[1] = 1
        year.append(str(start_n[0]) + "년" + str(start_n[1]) + "월")
        if(start_n[0] == int(finish.split('/')[0]) and start_n[1] == int(finish.split('/')[1])):
           break

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/NanumGothic.ttf").get_name()
rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False
df = pd.read_csv('아파트/result.csv',index_col=0,encoding="cp949")
df2 = pd.read_csv('수도권_변동률.csv',index_col=0,encoding="cp949")
df3 = pd.read_csv('경기도_변동률.csv',index_col=0,encoding="cp949")


df1 = df['sinbundang'][95:144]
df2 = df2['value'][95:144]
df3 = df3['value'][95:144]
print(df2)
plot = df1.plot(color='red', label='신분당선')
plot = df2.plot(color='blue', label='수도권')
plot = df3.plot(color='black', label='경기도')
year= []
getYear('2014/1', '2018/1', year)
print(year)



#x_value = [2006-2, 2006-3, 2006-4, 2006-5]
#xticks = pd.date_range('2006 2', '2006 7', freq='M')

#plt.xticks(xticks, [x.strftime('%Y %m') for x in xticks])
plot.set_xlabel("년도/월")
plot.set_ylabel("변동률")
x = numpy.arange(len(year))

#plt.xlim(['2006 2','2006 7'])
#plt.yticks([-1,0,1])
plt.xticks(x, year,
           fontsize=10, 
           rotation=45)
plt.ylim([-1,1])

#구간강조
plt.axvspan(23, 24, facecolor='#FFB6C1')

#라벨 달아주기
plt.legend()
#plt.plot(x_value, df)
plt.title("신분당선")
plt.show()

