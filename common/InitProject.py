import time
import unittest
from naname import name
import random
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from page_locators.login_locator import LoginLocator as LL
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
role = ['"admin"', '"操作员"', '"操作级"']
ls = [1, 2, 3, 4, 5, 6]
sex = ['"男"','"女"']
class LoginPage():

    def __init__(self):
        self.driver = webdriver.Chrome(options=options)  # 实例化一个浏览器对象
        # self.driver.implicitly_wait(10)
        # self.driver.maximize_window()
        # sleep(1)
        # self.driver = webdriver.Chrome()
    def get_url(self):
        self.driver.get('http://8.136.228.10/')
    def login(self):
        self.driver.find_element(By.XPATH, '//input[@name="username"]').send_keys('zglt_admin')
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('aic123456')
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()  # 登录

    def crate_users(self,num1,num2):
        for i in range(num1, num2 + 1):
            self.driver.find_element(By.XPATH, '//span[text()="添加"]').click()
            sleep(1)
            sleep(0.5)
            self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[5]/section/div[1]/div[2]/div/div[2]/form/div/div[1]/div[1]/div/div[1]/input').send_keys(
                i)  # 登录名称
            sleep(0.5)
            self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[5]/section/div[1]/div[2]/div/div[2]/form/div/div[2]/div[1]/div/div/input').send_keys(
                name())  # 用户别名
            sleep(0.5)
            self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[5]/section/div[1]/div[2]/div/div[2]/form/div/div[2]/div[2]/div/div[1]/input').send_keys(
                i)  # 用户编码
            sleep(0.5)
            self.driver.find_element(By.XPATH,'//form/div/div/div[4]/div/div/div/input[@class="el-input__inner"]').click()  # 角色
            sleep(0.5)
            self.driver.find_element(By.XPATH, '//span[text()=%s]' % (random.choice(role))).click()
            sleep(0.5)
            self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[5]/section/div[1]/div[2]/div/div[2]/form/div/div[2]/div[4]/div/div/div/div[2]/input').click()
            sleep(0.5)
            self.driver.find_element(By.XPATH,'//*[@id="app-body"]/div[last()]/div[2]/div[2]/div[%d]/div/label/span/span' % (random.choice(ls))).click()  # 岗位选择
            sleep(0.5)
            self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[5]/section/div[1]/div[2]/div/div[2]/form/div/div[1]/div[5]/div/div/div/div[2]/input').click()  # 职责
            sleep(0.5)
            self.driver.find_element(By.XPATH,'//*[@id="app-body"]/div[last()]/div[2]/div[2]/div[%d]/div/label/span/span' % (random.choice(ls))).click()
            self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[5]/section/div[1]/div[2]/div/div[2]/form/div/div[1]/div[6]/div/div/div/input').send_keys(i)
            # self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[5]/section/div[1]/div[2]/div/div[2]/form/div/div[2]/div[5]/div/div/div/input').click()  # 性别
            # self.driver.find_element(By.XPATH, '//span[text()=%s]' % (random.choice(sex))).click()
            sleep(0.5)
            self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[5]/section/div[1]/div[2]/div/div[3]/div/button[2]/span').click()  # 确定
            sleep(2)
