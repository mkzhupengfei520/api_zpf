from time import sleep
from selenium import webdriver
from module import baidumodule
driver = webdriver.Firefox(
    executable_path="C:\\Users\\HP\\Documents\\WeChat Files\\ZPF1277129486\\Files\\geckodriver.exe")
start = baidumodule(driver)
#start.login("selenium")
#sleep(2)
#start.login("webdriver")
#sleep(2)
name = ["selenium0","selenium1","selenium2","selenium3"]
for i in name:
    start.login(i)
    sleep(2)
start.login_out()
