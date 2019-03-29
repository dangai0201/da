#-*-coding:utf-8-*-
import os,sys
os.getcwd()
sys.path.append(os.getcwd())
import time

from fz.fengzhuang import Login


class Gouwuche():
    def __init__(self):
        self.driver=Login().driver
    def xiugai1(self):
        self.driver.find_elements_by_class_name("f6")[0].click()
    def xiugai2(self,mingzi,dizhi,tel,email,youbian,shoujihao):
        self.driver.find_elements_by_name("f6")[1].click()
        self.driver.find_element_by_name("consignee").send_keys(mingzi)
        self.driver.find_element_by_name("address").send_keys(dizhi)
        self.driver.find_element_by_name("tel").send_keys(tel)
        self.driver.find_element_by_name("email").send_keys(email)
        self.driver.find_element_by_name("zipcode").send_keys(youbian)
        self.driver.find_element_by_name("mobile").send_keys(shoujihao)
        self.driver.find_elements_by_class_name("bnt_blue_2")[0].click()

    def shiyongyue(self,a):
        self.driver.find_element_by_name("surplus").send_keys(a)

    def shiyongjifen(self,a):
        self.driver.find_element_by_name("integral").send_keys(a)

    def shiyonghongbao(self,a):
        self.driver.find_element_by_name("bonus_sn").send_keys(a)
        self.driver.find_element_by_name("validate_bonus").click()

    def dingdanfuyan(self,a):
        self.driver.find_element_by_name("postscript").send_keys(a)


    def peisongshifou(self):
        self.driver.find_element_by_name("need_insure").click()

    def tijiaodingdan(self):
        self.driver.find_element_by_xpath("//*[@id=\"theForm\"]/div[11]/div[2]/input[1]").click()





