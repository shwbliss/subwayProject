#막대그래프 시각화

import matplotlib
from matplotlib import pyplot
import numpy
import pandas as pd
from itertools import count
from matplotlib import font_manager, rc


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
df1 = df['uisinseol'][31:55]
print(df1)
year= []
getYear('2008/9', '2010/9', year)
pyplot.figure()

x = numpy.arange(len(year))

pyplot.bar(x-0.0, df1, label='우이신설', width=0.8, color='green')
pyplot.xticks(x, year,fontsize=10,rotation=45)
#개통발표시점
pyplot.axvspan(11, 12, facecolor='#FFB6C1')
pyplot.legend()
pyplot.xlabel('년도/월')
pyplot.ylabel('변동률')
pyplot.ylim(-0.2, 0.2)
pyplot.title('우이신설')

pyplot.show()


