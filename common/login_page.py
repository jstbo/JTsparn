import time
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from page_locators.login_locator import LoginLocator as LL

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()


    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LL.username_loc))
        self.driver.find_element(*LL.username_loc).send_keys(username)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LL.password_loc))
        self.driver.find_element(*LL.password_loc).send_keys(password)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LL.loginbtn_loc))
        self.driver.find_element(*LL.loginbtn_loc).click()

    def is_exist_logout(self):
        """
        判断退出按钮,是否可见
        :return:
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LL.logout_loc))
            return True
        except Exception as e:
            return False

    def get_login_errmsg_text(self):
        """
        定位输入反向数据时, 提示文本
        :return:
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LL.login_err_loc))
        text = self.driver.find_element(*LL.login_err_loc).text
        return text

    def is_alert_exist(self):
        """
        判断javascript弹窗提示是否可点击
        :return:
        """
        try:
            time.sleep(1)
            self.driver.switch_to.alert.accept()
            return  True
        except Exception as e:
            return  False