
# coding: utf-8

# In[ ]:

#该程序用于从金证官网抓取社招的职位信息


# In[3]:

from bs4 import BeautifulSoup


# In[4]:

import requests


# In[5]:

urlpage=requests.get('http://www.szkingdom.com/publisher/SocialRecruit.html')
urlpage.encoding='utf-8'
urltx=urlpage.text
#print(urltx)


# In[192]:

soup=BeautifulSoup(urltx,"lxml")


# In[193]:

myfile=open("c:\\job.txt","w")


# In[194]:

#print ( soup.prettify() )


# In[195]:

#print(soup.body.contents[6])


# In[196]:



#for child in soup.body.contents[6].descendants:
    #print (child)



# In[197]:

soup2 = soup.body.contents[6]


# In[198]:

for i in range(0,len(soup2.div.contents)):
    souptemp = soup2.div.contents[i]   
    try:        
        soupdiv=souptemp.nextSibling.nextSibling.nextSibling
        try:
            for j in range(1,len(soupdiv.contents)):     
                try:
                    #print (soupdiv.contents[j])
                    soupclass = soupdiv.contents[j]
                    str =''
                    for sibling in soupclass.span.next_siblings:
                       # print(sibling.string)
                        str += sibling.string.strip()
                        str +=','
                    #print(repr(str) )
                    #str.strip()
                    print(str)
                    myfile.write(str)
                    myfile.write("\n")
                    #print(repr(str) )
                       
                except:
                    pass
        except:
            pass
    except:
        pass
   # print(souptemp.nextSibling.nextSibling.nextSibling)

#print(soup2.div.contents)
# In[199]:

myfile.close()


# In[ ]:



