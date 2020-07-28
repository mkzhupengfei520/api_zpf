# coding: utf-8
from itertools import islice
from time import sleep
from selenium import webdriver
from module import baidumodule

csv_file = "D:\\file\\file.csv"

driver = webdriver.Firefox(executable_path=
                           "C:\\Users\\HP\\Documents\\WeChat Files\\ZPF1277129486\\Files\\geckodriver.exe")
start = baidumodule(driver)
with open(csv_file, "r") as name:
    lines = name.readlines()
for i in islice(lines, 1, None):
    start.login(i)
    sleep(2)
start.login_out()
