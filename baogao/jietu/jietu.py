from PIL import ImageGrab
import time

class Jietu():
    def jiequtupian(self):
        picture_time = time.strftime("%Y-%m-%d ", time.localtime(time.time()))
        pic = ImageGrab.grab()
        pic.save('/Users/yuliguo/PycharmProjects/py3.7lianxi/baogao/jietu/' + picture_time + '.png')
        pass
# Jietu().jiequtupian()