#-*-coding:utf-8-*-
import xlwings
class Huoquexel():
    #读取exel
    def duquexel(self,weizhi):
        xw=xlwings
        #打开一个已存在的xlxs文件
        a=xw.Book("../duquexcl/execl.xlsx")
        #获取sheet页名
        b=a.sheets['denglu']
        #读取数据
        c=b.range(weizhi).value
        return c
#Huoquexel().duquexel("F3","DJSDNASD")
    #写入exel
    def xieruexel(self,weizhi,neirong):
        xw = xlwings  # 打开一个已存在的xlxs文件
        a = xw.Book("../duquexcl/execl.xlsx")
        # 获取sheet页名
        b = a.sheets['denglu']

        # 读取数据
        # c=b.range('D2').value
        # 写入数据
        # c=b.range('F2').value='ABCD'
        c = b.range(weizhi).value = neirong
        a.save()

        return c





#print Huoquexel().duquexel("E4")
#
# print type(Huoquexel().duquexel())