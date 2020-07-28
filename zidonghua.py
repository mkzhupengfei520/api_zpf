# -*- coding:UTF-8 -*-
from selenium import webdriver
import time
import os
driver = webdriver.Firefox(executable_path="C:\\Users\\HP\\Documents\\WeChat Files\\ZPF1277129486\\Files\\geckodriver.exe")
driver.maximize_window()#窗口最大化
time.sleep(2)
driver.get("https://testsxhadmin.shixiangyiwei.com/adminuser/login.html")
driver.find_element_by_id("admin_user_name").send_keys("zhupengfei383")  #用户名
driver.find_element_by_id("admin_user_password").send_keys("123123a@")#密码a
driver.find_element_by_id("checkcode").send_keys("aa040128$")#万能验证码
driver.find_element_by_id("validate-submit").click()#登录按钮
alter1=driver.switch_to_alert()
alter1.accept()
time.sleep(2)
driver.find_element_by_xpath("//aside[@id='nav']//a[@class='auto']//span[text()='模板管理']").click()#模板管理
time.sleep(2)
driver.find_element_by_xpath("//aside[@id='nav']//a[@class='auto menu-li']//span[text()='模板查询']").click()#模板查询
time.sleep(2)
driver.find_element_by_xpath("//section[@id='content']//a[@class='btn btn-primary']").click()#新增按钮
time.sleep(2)
driver.find_element_by_xpath("//section[@id='content']//div[@class='col-sm-6 am-u-md-6']//img[@class='am-img-responsive img' and@alt='foundation']").click()#社区自提
time.sleep(2)
#driver.find_element_by_id("share_title").send_keys("selenium")
#name = ["模板1", "模板2", "模板3"]
#string = "模板1".decode("utf-8")
#driver.find_element_by_id("share_title").send_keys(string)
ten=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
driver.find_element_by_id("share_title").send_keys(ten)
time.sleep(2)
driver.find_element_by_xpath("//input[@id='adv']//parent::div").click()#选择文件
time.sleep(2)
#os.system("C:\Users\HP\Desktop\shangchuan.exe")
os.system(r'C:\Users\HP\Desktop\UploadPic.exe')










