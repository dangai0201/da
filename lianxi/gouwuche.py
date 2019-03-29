#-*-coding:utf-8-*-
import os,sys
os.getcwd()
sys.path.append(os.getcwd())
import time

from fz.fengzhuang import Login


class Gouwuche():
    def __init__(self):
        self.driver=Login().driver



    def shangpinmingcheng(self):
        a=self.driver.find_element_by_xpath("//*[@id=\"formCart\"]/table[1]/tbody/tr[2]/td[1]/a[2]").text
        return a

    def shichangjia(self):
        a=self.driver.find_element_by_xpath("//*[@id=\"formCart\"]/table[1]/tbody/tr[2]/td[3]").text
        return a
    def bendianjia(self):
        a=self.driver.find_element_by_xpath("//*[@id=\"formCart\"]/table[1]/tbody/tr[2]/td[4]").text
        return a
    def xiugaishuliang(self,a):
        self.driver.find_elements_by_class_name("inputBg")[0].clear()
        self.driver.find_elements_by_class_name("inputBg")[0].send_keys(a)
        


    def dianjishanchu(self):
        self.driver.find_element_by_xpath("//*[@id=\"formCart\"]/table[1]/tbody/tr[2]/td[7]/a[1]").click()

    def dianjifangrugouwuche(self):
        self.driver.find_element_by_xpath("//*[@id=\"formCart\"]/table[1]/tbody/tr[2]/td[7]/a[2]")

    def qingkonggouwuche(self):
        self.driver.find_elements_by_class_name("bnt_blue_1")[0].click()
    def gengxingouwuche(self):
        self.driver.find_elements_by_class_name("bnt_blue_1")[1].click()




    def dianjijiesuan(self):
        self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/table/tbody/tr/td[2]/a/img").click()

    def dianjijixugouwu(self):
        self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/table/tbody/tr/td[1]/a/img").click()

