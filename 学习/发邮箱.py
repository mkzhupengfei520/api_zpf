#发邮件的库
import smtplib

#邮件文本
from  email.mime.text import MIMEText

#SMTP服务器
from Tools.demo.mcast import sender

SMTPserver = "smtp.163.com"

#发邮件的地址
Sender = "wangman19951205@163.com"

#发送者邮箱的密码
passwd = "zpf563292"

#设置发送的内容
message = "沙雕王满，爸爸来看你了"
mag = MIMEText(message)

#标题
mag["Subject"] = "www"

#收件者
mag["From"] = Sender

#创建SMTP服务器
mailServer = smtplib.SMTP(SMTPserver, 25)

#登陆邮箱
mailServer.login(Sender, passwd)

#发送邮件
mailServer.sendmail(Sender, ["wangman19951205@163.com"], mag.as_string())
#推出邮箱
mailServer.quit()





