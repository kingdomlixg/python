
# coding: utf-8

# In[85]:

get_ipython().magic('pwd')


# In[53]:

#本程序用于从kcbpcli的调试日志dat文件中，找出mac地址，并打印


# In[54]:

import os


# In[55]:

myfile = open("c:\\034FCFBC.dat","r");


# In[56]:

mylist=[]
#print(mylist.count('goodb'))
while True:  
    line=myfile.readline()
    #print(len(line))
    if not line: 
        break
    #print(line)
    #mac地址是从74位开始取12位
    strTemp=line[74:86]
    #print(mylist.count('good'))
    if (mylist.count(strTemp) ) <1:
        mylist.append(strTemp)
        
print(mylist)
        
    
            
    


# In[57]:

myfile.close()


# In[ ]:



