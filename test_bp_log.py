
# coding: utf-8

# In[85]:

get_ipython().magic('pwd')


# In[86]:

#本程序用于从kcbpcli的调试日志dat文件中，找出业务调用失败的日志信息，记录到文件中


# In[109]:

import os


# In[110]:

myfile = open("c:\\034FCFBC.dat","r");


# In[111]:

myfile3= open("c:\\034FCFBC.dat","r");


# In[112]:

myfile2 = open("c:\\errlog.txt","w");


# In[113]:

while True:  
    line=myfile.readline()
    #print(len(line))
    if not line: 
        break
    #print(line)
    strTemp=line[:40]
    if strTemp.find("recv")>=0:
        #print(line[232])
        #查看日志看到232是收到的code的位置
        if line[232]!='0':
            #print(line) 
            #再开一个文件句柄，读取错误的请求信息
            myfile3.seek(myfile.tell()-1000,0)
            line2=myfile3.read(700)
            myfile2.writelines(line2)
            myfile2.writelines("\n")
            #print(line2)
            myfile2.writelines(line)
            
    


# In[114]:

myfile.close()


# In[115]:

myfile2.close()


# In[116]:

myfile3.close()


# In[ ]:



