#该例子程序从KCBP的授权工具MakeLic的日志文件license.log中找出关键信息，记录到数据库
#中

#数据库语句create table bp_license(companyname varchar(64),expire int,license_time  varchar(64))
import pyodbc
myfile=open("c:\\license.log",encoding='gb18030',errors='ignore')

conn = pyodbc.connect(r'DRIVER={SQL Server Native Client 11.0};SERVER=10.201.64.249;DATABASE=test;UID=123;PWD=123')
cursor = conn.cursor()

cursor.execute("delete from bp_license")
i=1
print("数据导入开始")
for i in range(4000):
    line=myfile.readline()
    if len(line)<10:
        break
    i = i+1
    mylist = line.split( )
    #print(mylist)
    

    tempname = mylist[1]
    #print(tempname)
    #list2 = tempname.split('=')
    strname=(tempname.split('=') )[1]
    #print( strname)
    #print(line.split( ))


    if strname.find("123")>=0 or strname.find("test")>=0 or strname.find("金证股份")>=0 or strname.find("证券软件")>=0 or strname.find("研发中心")>=0:
        continue

    temptime=mylist[4]
    time=(temptime.split('=') )[1]
    #print(time)

    licensetime2= mylist[0]
    licensetime=licensetime2.replace('[','')
    licensetime=licensetime.replace("]"," ",5)
    #print(licensetime)


    cursor.execute("insert into bp_license(companyname, expire,license_time) values (?,?,?)",strname,time,licensetime)
    conn.commit()

print("数据导入完成")

myfile.close()
