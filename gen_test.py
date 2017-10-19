#该例子程序用于生成kcbptest的410503的压测串
import os
myfile = open("c:\\410503.txt","w")
for i in range(1,100):
    myfile.write("410503!netaddr:127.0.0.1,orgid:5711,ext:0,serverid:5,operid:,operpwd:,operway:3,custid:571100000015,custorgid:5711,trdpwd:Pf4DwoHxo4Qfyww0xcr5LQ==,custcert:,funcid:410503,market:,secuid:,stkcode:,fundid:571100000015,qryflag:1,count:1000,poststr:\n")

myfile.close()
    
