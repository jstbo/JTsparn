import unittest
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from naname import name
# bs.find_element_by_xpath('//*[@id="password"]').send_keys("12345678", Keys.ENTER)#输入密码并回车
def init():
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
    driver = webdriver.Chrome(options=options)
    # driver.back()
    return driver
def get_url():
    init().implicitly_wait(20)
    url = 'http://8.136.228.10/'
    init().get(url)
    # driver.maximize_window()
    locator = (By.XPATH,'//button[@type="submit"]')
    WebDriverWait(init(),20,1).until(EC.presence_of_element_located(locator))

def login():
    init().find_element(By.XPATH,'//input[@name="username"]').send_keys('zglt_admin')
    init().find_element(By.XPATH,'//input[@name="password"]').send_keys('aic123456')
    init().find_element(By.XPATH,'//button[@type="submit"]').click()   # 登录
def sys_man():
    init().find_element(By.XPATH,'//ul[@class="el-menu"]/child::div[2]').click()    # 打开系统管理
    sleep(1)
    init().find_element(By.XPATH,'//ul[@class="el-menu"]/child::div[2]/li/ul/div[2]').click()    # 打开权限管理
    sleep(1)
    init().find_element(By.XPATH,'//ul[@class="el-menu"]/child::div[2]/li/ul/div[2]/li/ul/div[7]').click()    # 打开用户管理
    sleep(1)
role = ['"admin"', '"操作员"','"操作级"']
ls = [1,2,3,4,5,6]
sex = ['"男"','"女"']
def create_user(num):
    for i in range(1050,num+1050):
        init().find_element(By.XPATH,'//span[text()="添加"]').click()
        sleep(1)
        sleep(0.5)
        init().find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[5]/section/div[1]/div[2]/div/div[2]/form/div/div[1]/div[1]/div/div[1]/input').send_keys(i) #登录名称
        sleep(0.5)
        init().find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[5]/section/div[1]/div[2]/div/div[2]/form/div/div[2]/div[1]/div/div/input').send_keys(name())  #用户别名
        sleep(0.5)
        init().find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[5]/section/div[1]/div[2]/div/div[2]/form/div/div[2]/div[2]/div/div[1]/input').send_keys(i)  #用户编码
        sleep(0.5)
        init().find_element(By.XPATH,'//form/div/div/div[4]/div/div/div/input[@class="el-input__inner"]').click()  #角色
        sleep(0.5)
        init().find_element(By.XPATH,'//span[text()=%s]'%(random.choice(role))).click()
        sleep(0.5)
        init().find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[5]/section/div[1]/div[2]/div/div[2]/form/div/div[2]/div[4]/div/div/div/div[2]/input').click()
        sleep(0.5)
        init().find_element(By.XPATH,'//*[@id="app-body"]/div[last()]/div[2]/div[2]/div[%d]/div/label/span/span'%(random.choice(ls))).click() #岗位选择
        sleep(0.5)
        init().find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[5]/section/div[1]/div[2]/div/div[2]/form/div/div[1]/div[5]/div/div/div/div[2]/input').click() #职责
        sleep(0.5)
        init().find_element(By.XPATH,'//*[@id="app-body"]/div[last()]/div[2]/div[2]/div[%d]/div/label/span/span'%(random.choice(ls))).click()
        init().find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[5]/section/div[1]/div[2]/div/div[2]/form/div/div[1]/div[6]/div/div/div/input').send_keys(i)
        init().find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[5]/section/div[1]/div[2]/div/div[2]/form/div/div[2]/div[5]/div/div/div/input').click() #性别
        init().find_element(By.XPATH,'//span[text()=%s]'%(random.choice(sex))).click()
        sleep(0.5)
        init().find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[5]/section/div[1]/div[2]/div/div[3]/div/button[2]/span').click() #确定
        sleep(2)







