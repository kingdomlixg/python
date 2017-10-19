#coding=utf-8

import pandas as pd
# Reading data from web
#data_url = "https://raw.githubusercontent.com/alstat/Analysis-with-Programming/master/2014/Python/Numerical-Descriptions-of-the-Data/data.csv"
#df = pd.read_csv(data_url)

#print (df.head() )
file_name="c:\\456.csv"
delimiter="\t"
df2 = pd.read_csv(file_name)
print(df2.head())



count = 0
i=0
while i < 127:
   strTemp = df2.ix[i,1]
   i = i + 1
   if(strTemp.find("革") >= 0):
        count = count+1
        print(strTemp)
   else:
        continue
            

       

print(count)
