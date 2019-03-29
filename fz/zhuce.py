#-*-codin:utf-8-*-
import os,sys
os.getcwd()
sys.path.append(os.getcwd())
from fz.fengzhuang import Login
import time




class Zhuce():
    def __init__(self):
        self.driver = Login().driver
    def zhuce001(self):
        self.driver.find_element_by_xpath("//*[@id=\"ECS_MEMBERZONE\"]/a[2]").click()
        time.sleep(2)
        pass
    def zhuce(self,name,email,password,password2,qq,bangong,jiating,shoujihao,wenti):
        self.driver.find_element_by_name("username").send_keys(name)
        self.driver.find_element_by_name("email").send_keys(email)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_name("confirm_password").send_keys(password2)
        self.driver.find_element_by_name("extend_field2").send_keys(qq)
        self.driver.find_element_by_name("extend_field3").send_keys(bangong)
        self.driver.find_element_by_name("extend_field4").send_keys(jiating)
        self.driver.find_element_by_name("extend_field5").send_keys(shoujihao)
        self.driver.find_element_by_name("passwd_answer").send_keys(wenti)

    def question(self,a=None):
        if a!=None:
            self.driver.find_element_by_name("sel_question").click()
            time.sleep(2)
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div[3]/div[1]/form/table/tbody/tr[10]/td[2]/select/option["+str(a)+"]").click()



    def submit(self):
        self.driver.find_element_by_name("Submit").click()






