#-*-coding:utf-8-*-
import xlwings


class Huoquexel():
    #读取exel
    # def duquexel(self):
    #     xw=xlwings
    #     #打开一个已存在的xlxs文件
    #     a=xw.Book("../duquexcl/execl.xlsx")
    #     #获取sheet页名
    #     b=a.sheets['denglu']
    #
    #     #读取数据
    #     c=b.range("C2").value
    #     return  c

    def xieruexel(self,):
        xw = xlwings  # 打开一个已存在的xlxs文件
        a = xw.Book("../duquexcl/execl.xlsx")
        # 获取sheet页名
        b = a.sheets['denglu']

        # 读取数据
        # c=b.range('D2').value



        # 写入数据
        # c=b.range('F2').value='ABCD'
        c = b.range('F2').value = "1234"
        a.save()
        return c

print Huoquexel().xieruexel()

# print Huoquexel().duquexel()
#
# print type(Huoquexel().duquexel())