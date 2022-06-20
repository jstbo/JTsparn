import aircv
import pyautogui
import time
import random
from InitProject import LoginPage
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from naname import name
def screen(x=1920, y=1080):
    """
    屏幕截图
    :param x: 横坐标
    :param y: 纵坐标
    :return:
    """
    pyautogui.screenshot('screen.png', region=(0, 0, x, y))
    return 'screen.png'


def click_element(src_image, dst_image, offset_x=0, offset_y=0):
    """
    基于图像查找点击
    :param src_image:
    :param dst_image:
    :param offset_x:
    :param offset_y:
    :return:
    """
    src_image = aircv.imread(src_image)
    dst_image = aircv.imread(dst_image)
    result = aircv.find_template(src_image, dst_image)
    print(result)
    # {'result': (828.0, 597.5), 'rectangle': ((804, 582), (804, 613), (852, 582), (852, 613)), 'confidence': 1.0}
    x, y = result.get('result')
    # print(y)
    # print(type(y))
    if result.get('confidence') > 0.85:
        if y > 950:
            # pyautogui.moveTo(100, 500, duration=0.25)
            # sleep(1)
            # print("y大于900，向下滑动滚轮")
            pyautogui.click(x + offset_x, y + offset_y)
            # sleep(1)
            pyautogui.scroll(-500)
            sleep(1)
        else:
            # print('y小于900')
            pyautogui.click(x + offset_x, y + offset_y)
    else:
        print('没找到图片')

def input_text_pos(x, y, text):
    """
    在坐标处输入文本
    :param x:
    :param y:
    :param text:
    :return:
    """
    pyautogui.click(x, y)
    pyautogui.write(text)


def input_text_image(dst_image, text, offset_x=0, offset_y=0):
    src_image = screen()
    click_element(src_image, dst_image, offset_x, offset_y)
    pyautogui.write(text)
def click_image(dst_image,offset_x=0, offset_y=0):
    src_image = screen()
    click_element(src_image, dst_image, offset_x, offset_y)



time.sleep(5)
# action.login()
# # 基于图像查找图片后点击偏移位置，并输入
# input_text_image('photos/xitongguanli.png', 'abc')
# click_image('1.png')
LoginPage().get_url()
LoginPage().login()
sleep(5)
click_image('photos/xitongguanli.png')
time.sleep(0.5)
click_image('photos/quanxianguanli.png')
time.sleep(0.5)
click_image('photos/yonghuguanli.png')
sleep(0.5)
LoginPage().crate_users(2011,2014)
click_image('photos/refresh.png')
sleep(3)
click_image('photos/dianjianguanli.png')
time.sleep(0.5)
click_image('photos/dianjianpeizhi.png')
time.sleep(0.5)

    # input_text_image('pwd.png', 'abc', offset_y=45)
    # 点击登录
    # click_element(screen(), 'login_button.png')

# click_image('photos/xitongguanli.png')
# pyautogui.moveTo(100, 500, duration=0.25)
# sleep(1)
# pyautogui.scroll(-1000)