#-*-coding:utf-8-*-
import os,sys
os.getcwd()
sys.path.append(os.getcwd())
from selenium import webdriver
import  time
import csv
import os
from fz.fengzhuang import Login




# dr=Login().driver
# import sys
#
# reload(sys)
# sys.setdefaultencoding( "utf-8" )

# 读取本地CSV文件
# f = csv.reader(open("aaa.csv", "rU"))
# for b in f:
#     print b[1]

class Duqucsv():
    def duqucsv(self):
        f = csv.reader(open("duqucsv/aaa.csv", "rU"))
        for a in f :
            return a[0]



print Duqucsv().duqucsv()

#csv 写入








# a = 'i am request,\xE6\x88\x91\xE6\x98\xAF\xE8\xAF\xB7\xE6\xB1\x82'.decode('utf-8').encode('utf-8')
# print a