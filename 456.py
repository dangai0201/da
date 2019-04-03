from PIL import ImageGrab
import time


picture_time = time.strftime("%Y-%m-%d-%H_%M", time.localtime(time.time()))
#全屏
# pic = ImageGrab.grab()
# pic.save('/Users/yuliguo/PycharmProjects/py3.7lianxi/baogao/jietu'+picture_time+ '.png')



#通过ctr+alt+a来实现的截图
# 可以实现 printscreen 按键，获取全屏截图
pic = ImageGrab.grabclipboard()
pic.save('/Users/yuliguo/PycharmProjects/py3.7lianxi/baogao/jietu'+picture_time+ '.png')


# 输入屏幕左上角和右下角的坐标
pic = ImageGrab.grab(bbox=(0, 0, 100, 100))
pic.save('/Users/yuliguo/PycharmProjects/py3.7lianxi/baogao/jietu'+picture_time+ '.png')



# 通过 printscreen 获取全屏截图
pic = ImageGrab.grabclipboard()
pic_mini = pic.crop(box=(200,200,400,400))
pic_mini.save(r"D:\tmp\save_min.jpg")





#第二种截图方法
# # -*- coding:utf-8 -*-
# from selenium import webdriver
# from time import sleep
# import time
#
#
# # 时间格式进行格式化
# def time_format():
#     current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
#     return current_time
#
#
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com/')
# driver.get_screenshot_as_file("截图\\" + time_format() + ".png")
#
# sleep(2)
# driver.quit()

