# coding=utf-8
from selenium import webdriver

class RunFFTest():
    def testMethod(self):
        driver = webdriver.Firefox(
            executable_path="C:\\Users\\HP\\Documents\\WeChat Files\\ZPF1277129486\\Files\\geckodriver.exe")
        driver.get("https://www.baidu.com/")


ff = RunFFTest()
ff.testMethod()
