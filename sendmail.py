#以下是Python发邮件的测试例子
import smtplib  
import email.mime.multipart  
import email.mime.text  
  
msg=email.mime.multipart.MIMEMultipart()  
msg['from']='lixg@szkingdom.com'  
msg['to']='lixg@szkingdom.com'  
msg['subject']='test'  
content=''''' 
    你好， 
            这是一封自动发送的邮件。 
 
        www.ustchacker.com 
'''  
txt=email.mime.text.MIMEText(content)  
msg.attach(txt)  
  
smtp=smtplib  
smtp=smtplib.SMTP()  
smtp.connect('smtp.szkingdom.com','25')  
smtp.login('lixg@szkingdom.com','Lixinge124612')  
smtp.sendmail('lixg@szkingdom.com','lixg@szkingdom.com',str(msg))  
smtp.quit()  
