#-*-coding:utf-8-*-

from fz.fengzhuang import Login

class Tijiaodingdan():
    def __init__(self):
        self.driver=Login().driver
    def tijiaodingdan(self):
        self.driver.find_element_by_xpath("//*[@id=\"theForm\"]/div[11]/div[2]/input[1]").click()
    def dingdanhao(self):
        a=self.driver.find_element_by_xpath("/html/body/div[5]/div/h6/font").text
        return a