#-*-coding:utf-8-*-
from fz.fengzhuang import Login

class Sousuo():
    def __init__(self):
        self.driver = Login().driver
    def sousuo(self,a):

        self.driver.find_element_by_name("keywords").clear()
        self.driver.find_element_by_name("keywords").send_keys(a)
        self.driver.find_element_by_class_name("fm_hd_btm_shbx_bttn").click()
