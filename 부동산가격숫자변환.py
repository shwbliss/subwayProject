#value값에 들어간 한글 '억' 제거하고 숫자로 변환

import pandas

df = pandas.read_csv('아파트\우이신설\종로청계힐스테이트.csv', encoding='cp949')


for i in range(0, df.shape[0]):
    
        #print(df['가격'][i])
        value = df['가격'][i].replace('억','').split()
        
        try:
            value[1] = value[1].replace(',','')
            
            if(len(value[1])==4):
                value = value[0]+value[1]
            elif(len(value[1])==3):
                value = value[0]+'0'+value[1]
            elif(len(value[1])==2):
                value = value[0]+'00'+value[1]
            elif(len(value[1])==1):
                value = value[0]+'000'+value[1]
        except:
            value = value[0]+'0000'
            
        df['가격'][i] = value
        print(df['계약일'][i]+'    '+value)
df.to_csv('아파트\우이신설\종로청계힐스테이트.csv', mode='w', encoding='cp949', index=False)
print(df)

        
