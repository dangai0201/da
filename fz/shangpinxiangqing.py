#-*-coding:utf-8-*-
import os,sys
os.getcwd()
sys.path.append(os.getcwd())
from fz.fengzhuang import Login

class Shangpinxiangqing():
    def __init__(self):
        self.driver = Login().driver
    def shangpinxiangqing(self,a):
        self.driver.find_element_by_id("number").clear()
        self.driver.find_element_by_id("number").send_keys(a)
        self.driver.find_element_by_class_name("btn_pink_138x32").click()
