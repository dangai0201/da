#-*-coding:utf-8-*-
import os,sys
os.getcwd()
sys.path.append(os.getcwd())
from selenium import webdriver
from fz.danli import singleton



@singleton
class Login():
    def __init__(self):
        #无效果化模式运行，后台运行
        # self.wutuxing=webdriver.ChromeOptions()
        # self.wutuxing.add_argument('--headless')
        # self.wutuxing.add_argument('--disable-gpu')
        # self.driver=webdriver.Chrome(options=self.wutuxing)




        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://192.168.43.133:811/ecshop/upload/")
        #print self.driver
