import aircv as ac
import time
import os
import pyautogui
# from action import init
""" 
待识别图片在截屏中的中心坐标，注：imgobj按1:1截图
"""
def acTap(path='photos/xitongguanli.png'):
    time.sleep(10)
    pic_time = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    dic_time = 'ScreenShot' + time.strftime('%Y-%m-%d', time.localtime(time.time()))
    # 创建截图文件夹
    try:
        File_Path = os.getcwd() + '\\' + dic_time
        if not os.path.exists(File_Path):
            os.makedirs(File_Path)
        else:
            pass
    except BaseException as msg:
        print("新建目录失败：%s" % msg)
    try:
        srcUrl = File_Path + '\\' + pic_time + '.png'  # 先保存文件URL
        pyautogui.screenshot(srcUrl)  # 截准备查找的整张页面，为了提高成功率，这里还可以指定区域截图
    except BaseException as pic_msg:
        print('截图失败：%s' % pic_msg)
    time.sleep(1)
    imgsrc = ac.imread(srcUrl)  # 打开查找页
    imgobj = ac.imread(path)  # 打开待识别的图片
    match_result = ac.find_all_template(imgsrc, imgobj, 0.8)  # 0.9是识别达标率
    print(match_result)
    # if match_result != None:
    #     x1, y1 = match_result[0]['result']  # 只取返回结果中第一个的中心坐标[(x,y)]，即识别成功率最高的坐标
    #     print(x1,y1)
    #     # self.driver.tap([(x1, y1)])  # 点击，如果需要多设备点击则需要对坐标进行转换
    #     pyautogui.click(x1,y1)
    # else:
    #     print('识别不到要点击的目标')

acTap()