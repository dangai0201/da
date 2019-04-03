from PIL import ImageGrab
import time


picture_time = time.strftime("%Y-%m-%d-%H_%M", time.localtime(time.time()))
#全屏
# pic = ImageGrab.grab()
# pic.save('/Users/yuliguo/PycharmProjects/py3.7lianxi/baogao/jietu'+picture_time+ '.png')



#通过ctr+alt+a来实现的截图
# # 可以实现 printscreen 按键，获取全屏截图
# pic = ImageGrab.grabclipboard()
# pic.save('/Users/yuliguo/PycharmProjects/py3.7lianxi/baogao/jietu'+picture_time+ '.png')


# # 输入屏幕左上角和右下角的坐标
# pic = ImageGrab.grab(bbox=(0, 0, 100, 100))
# pic.save('/Users/yuliguo/PycharmProjects/py3.7lianxi/baogao/jietu'+picture_time+ '.png')



# 通过 printscreen 获取全屏截图
# pic = ImageGrab.grabclipboard()
# pic_mini = pic.crop(box=(200,200,400,400))
# pic_mini.save(r"D:\tmp\save_min.jpg")





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




# #截图某个元素
# from selenium import webdriver
# from time import sleep
# import time
# from PIL import Image
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
# # 截取全屏
# driver.save_screenshot("/Users/yuliguo/PycharmProjects/py3.7lianxi/baogao/jietu/quanping.png")
# # 要截屏的目标元素
# element = driver.find_element_by_id("su")
# print(element.location)
# print(element.size)
# # 获取element的顶点坐标
# xPiont = element.location['x']
# yPiont = element.location['y']
# # 获取element的宽、高
# element_width = xPiont + element.size['width']
# element_height = yPiont + element.size['height']
#
# picture = Image.open(r'/Users/yuliguo/PycharmProjects/py3.7lianxi/baogao/jietu/quanping.png')
#
# '''
# crop()--  一个显式的参数：一个4元组
#   Image.crop(box=None):图像返回一个矩形区域,box是一个四元组 限定所述左，上，右，和下像素坐标
#   参数：box--裁剪矩形，作为（左，上，右，下）-tuple;返回类型：Image；返回：一个Image对象
#   所以你应该重写它：
#   img.crop((414,122,650,338))
#   #        ^    4-tuple    ^
# '''
# picture = picture.crop((xPiont, yPiont, element_width, element_height))
# picture.save("/Users/yuliguo/PycharmProjects/py3.7lianxi/baogao/jietu/jietu.png")
#
# sleep(2)
# driver.quit()


# 参考博客：https://blog.csdn.net/lykio_881210/article/details/79281982



