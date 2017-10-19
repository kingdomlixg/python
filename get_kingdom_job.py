#该程序用于从金证官网上抓取社招的职位和人数等信息
#http://www.szkingdom.com/publisher/SocialRecruit.html
import requests
urlpage=requests.get('http://www.szkingdom.com/publisher/SocialRecruit.html')
urlpage.encoding='utf-8'
urltx=urlpage.text
print(urltx)
