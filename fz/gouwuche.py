#-*-coding:utf-8-*-
import time

from fz.fengzhuang import Login

class Gouwuche():
    def __init__(self):
        self.driver=Login().driver
    def dianjijiesuan(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/table/tbody/tr/td[2]/a/img").click()


