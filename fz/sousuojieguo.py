#-*-coding:utf-8-*-
import os,sys
os.getcwd()
sys.path.append(os.getcwd())
from fz.fengzhuang import Login

class Sousuojieguo():
    def __init__(self):
        self.driver = Login().driver
    def sousuojieguo(self,a):
        #当id，class相同时
        self.driver.find_elements_by_class_name("goodsimg")[a].click()

