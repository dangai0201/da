#-*-coding:utf-8-*-
import time
from fz.fengzhuang import Login

import os,sys
os.getcwd()
sys.path.append(os.getcwd())







class Denglu():
    def __init__(self):
        self.driver = Login().driver
    def denglu(self,a,b):
        self.driver.find_element_by_xpath("//*[@id=\"ECS_MEMBERZONE\"]/a[1]").click()
        time.sleep(2)
        self.driver.find_element_by_name("username").send_keys(a)
        self.driver.find_element_by_name("password").send_keys(b)
        self.driver.find_element_by_name("submit").click()


    def alert(self):
        return self.driver.switch_to.alert



    def guanbi(self):
        self.driver.quit()
