#-*-coding:utf-8-*-
import os,sys
os.getcwd()
sys.path.append(os.getcwd())
import unittest
from fz.fengzhuang import Login
from fz.zhuce import Zhuce
from fz.denglu import Denglu
import time
from baogao.baogao import Baogao

import os,sys
os.getcwd()
sys.path.append(os.getcwd())

class ZHUCE(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        #所有用例执行前
        self.driver=Login().driver
        pass
    @classmethod
    def tearDownClass(self):
        Denglu().guanbi()
        pass
    def setUp(self):
        #每次用例执行前执行一次
        Zhuce().zhuce001()
        pass


    def tearDown(self):
        # Denglu().guanbi()
        pass

    #用例按照ascii顺序执行， 0-9 A-Z a-z

    def test_001(self):
        Zhuce().zhuce("dasds","dasdsad@qq.com","123456","","","","","18410178656","dalian")
        Zhuce().question(6)
        Zhuce().submit()
        time.sleep(2)
        self.msg=Denglu().alert()
        shiji=self.msg.text
        yuqi=u"两次输入密码不一致"
        print (shiji)
        #点击确定按钮
        Denglu().alert().accept()
        self.assertIn(yuqi,shiji,msg=u"对比失败")
        pass
    def test_002(self):
        Zhuce().zhuce("dasds", "dasdsad@qq.com", "", "", "", "", "", "18410178656", "dalian")
        Zhuce().question(6)
        Zhuce().submit()
        time.sleep(2)
        self.msg = Denglu().alert()
        shiji = self.msg.text
        yuqi = u"登录密码不能为空"
        print(shiji)
        # 点击确定按钮
        Denglu().alert().accept()
        self.assertIn(yuqi, shiji, msg=u"对比失败")
        pass
    def test_003(self):
        # Zhuce().zhuce("", "", "", "", "", "", "", "", "")
        # Zhuce().question(6)
        Zhuce().submit()
        time.sleep(2)
        self.msg = Denglu().alert()
        shiji = self.msg.text
        yuqi = u"登录密码不能为空"
        print(shiji)
        # 点击确定按钮
        Denglu().alert().accept()
        self.assertIn(yuqi, shiji, msg=u"对比失败")

        pass
    def test_004(self):

        # Zhuce().question(6)
        self.driver.find_element_by_name("username").send_keys("123456")
        Zhuce().submit()
        time.sleep(2)
        self.msg = Denglu().alert()
        shiji = self.msg.text
        yuqi = u"登录密码不能为空"
        print(shiji)
        # 点击确定按钮
        Denglu().alert().accept()
        self.assertIn(yuqi, shiji, msg=u"对比失败")
        pass
if __name__ == '__main__':
    # unittest.main()
    Baogao().getbaogao(u"报告",u"ecshop",u"购物流程用例",unittest.makeSuite(ZHUCE))


