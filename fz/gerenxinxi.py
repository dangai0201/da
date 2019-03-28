#-*-coding:utf-8-*-

from fz.fengzhuang import Login

class Genrenxinxi():
    def __init__(self):
        self.driver=Login().driver
    def gerenxinxi(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/a[1]").click()

    def zuixindingdan(self):
        self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/div/div/a[3]").click()
        a=self.driver.find_element_by_class_name("f6").text
        return a