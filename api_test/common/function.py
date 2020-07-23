#coding:utf-8
import os,unittest,time
from HTMLTestReportCN import HTMLTestRunner
from email.mime.text import MIMEText#email模块下有mime包
from email.mime.multipart import MIMEMultipart
import os,smtplib#主要负责发送邮件：是一个发送邮件的动作，连接邮箱服务器，登录邮箱，发送邮件（有发件人，收信人，邮件内容）。



class Test_init():
    def add_case(self,cur_path="case",caseName = "case", rule = 'test*.py'):
        case_path = os.path.join(cur_path,caseName)
        if not os.path.exists(case_path):
            os.mkdir(case_path)
            #自动根据测试目录start_dir匹配查找测试用例文件
        discover = unittest.defaultTestLoader.discover(case_path,
                                                       pattern=rule,top_level_dir=None)
        return discover


    def run_case(self,cur_path,all_case,reportName = 'report'):
        report_path = os.path.join(cur_path,reportName)
        if not os.path.exists(report_path):
            os.mkdir(report_path)
        now = time.strftime('%Y-%m-%d-%H.%M.%S',time.localtime(time.time()))
        report_abspath = os.path.join(report_path,now+"-TestReport.html")
        fp = open(report_abspath,"wb")
        runner = HTMLTestRunner(stream=fp,
                                                 title=u'自动化测试报告',
                                                 description=u'用例执行情况',
                                                 tester='pengfei.zhu')
        runner.run(all_case)
        fp.close()
    def get_report_file(self,report_path):  #拼接文件路径
        lists = os.listdir(report_path) #os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
        lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path,fn)))
        report_file = os.path.join(report_path,lists[-1])
        return report_file

    def send_mail(self,sender,psw,receiver,smtpserver,report_file,port):
        with open(report_file,"rb") as f:
            mail_body = f.read()  #读取的内容
        msg =MIMEMultipart()
        body = MIMEText(mail_body,_subtype='html',_charset='utf-8') #保证多语言兼容性。
        msg['Subject'] = u'自动化测试报告'#邮件主题
        msg['from'] = sender #发送者
        msg['to'] = receiver  #接收者，msg 是字符串，表示邮件
        msg.attach(body)
        att = MIMEText(open(report_file,"rb").read(),"base64","utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename="report.html"'
        msg.attach(att)
        print (smtpserver,psw,sender,receiver,port)
        try:
            smtp = smtplib.SMTP_SSL(str(smtpserver),str(port))
        except:
            print('error')
            smtp = smtplib.SMTP()
            smtp.connect(str(smtpserver),str(port))
        smtp.login(str(sender),str(psw))
        smtp.sendmail(sender,receiver,msg.as_string())
        smtp.quit()

