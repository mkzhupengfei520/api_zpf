# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Page(object):
    """基础类，用于所有页面对象类继承"""
    login_url = 'https://i.qq.com'

    def __init__(self, selenium_driver, base_url=login_url):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'did not land on %s' % url

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)


class LoginPage(Page):
    """登录页面模型"""

    url = '/'
    # 定位器
    username_loc = (By.ID, 'u')
    password_loc = (By.ID, 'p')
    submit_loc = (By.ID, 'login_button')

    def type_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def type_submit(self):
        self.find_element(*self.submit_loc).click()


def test_user_login(driver, username, password):
    """测试获取的用户名、密码是否可以登录成功"""
    login_page = LoginPage(driver)
    login_page.open()
    driver.maximize_window()
    driver.switch_to_frame('login_frame')
    driver.find_element_by_id("switcher_plogin").click()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.type_submit()


def main():
    try:
        driver = webdriver.Firefox()
        username = 'qq号'  # 调试的时候需要换成对应的QQ号
        password = 'qq密码'  # 需要换成对应的密码
        test_user_login(driver, username, password)
        sleep(3)
        # 断言的方式判断登录是否成功
        try:
            assert '对应空间的title' in driver.title  # 调试时候title要换
            print ('successful')
        except Exception as e:
            print ('failed')

    finally:
        driver.close()


if __name__ == '__main__':
    main()



