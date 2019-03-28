#-*-coding:utf-8-*-

import unittest
import time
from fz.fengzhuang import Login
from fz.zhuce import Zhuce
from fz.denglu import Denglu
from duquxml.huoquxml import Duqu


class DENGLU(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = Login().driver
        pass

    @classmethod
    def tearDownClass(self):
        Denglu().guanbi()
        pass

    def setUp(self):

        pass

    def tearDown(self):
        # 通过try进行判断有没有弹框
        try:
            Denglu().alert().accept()
        except Exception:
            # print u"没有弹框"
            pass
        self.driver.find_element_by_xpath("//*[@id=\"ECS_MEMBERZONE\"]/a[2]").click()
        pass

    def test_001(self):
        i="1"
        print "test00"+i
        username = Duqu().duqu("lianxi", "denglu001", "username")
        password = Duqu().duqu("lianxi", "denglu001", "password")
        yuqi = Duqu().duqu("lianxi", "denglu001", "yuqi")
        if username==" ":
            username=""
        if password==" ":
            password=""
        Denglu().denglu(username, password)
        a = Denglu().alert()
        #a = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]")
        shiji = a.text
        print shiji
        self.assertIn(yuqi, shiji, msg=u"断言失败")
        pass
    def test_002(self):
        i="2"
        print "test00" + i
        username = Duqu().duqu("lianxi", "denglu00"+i, "username")
        password = Duqu().duqu("lianxi", "denglu00"+i, "password")
        yuqi = Duqu().duqu("lianxi", "denglu00"+i, "yuqi")
        if username==" ":
            username=""
        if password==" ":
            password=""
        Denglu().denglu(username, password)
        a = Denglu().alert()
        #a = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]")
        shiji = a.text
        print shiji
        self.assertIn(yuqi, shiji, msg=u"断言失败")
        pass
    def test_003(self):
        i="3"
        print "test00" + i
        username = Duqu().duqu("lianxi", "denglu00"+i, "username")
        password = Duqu().duqu("lianxi", "denglu00"+i, "password")
        yuqi = Duqu().duqu("lianxi", "denglu00"+i, "yuqi")
        if username==" ":
            username=""
        if password==" ":
            password=""
        Denglu().denglu(username, password)
        #a = Denglu().alert()
        a = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]")
        shiji = a.text
        print shiji
        self.assertIn(yuqi, shiji, msg=u"断言失败")
        pass
    def test_004(self):
        i="4"
        print "test00" + i
        username = Duqu().duqu("lianxi", "denglu00"+i, "username")
        password = Duqu().duqu("lianxi", "denglu00"+i, "password")
        yuqi = Duqu().duqu("lianxi", "denglu00"+i, "yuqi")
        if username==" ":
            username=""
        if password==" ":
            password=""
        Denglu().denglu(username, password)
        #a = Denglu().alert()
        a = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]")
        shiji = a.text
        print shiji
        self.assertIn(yuqi, shiji, msg=u"断言失败")
        pass
    def test_005(self):
        i="5"
        print "test00" + i
        username = Duqu().duqu("lianxi", "denglu00"+i, "username")
        password = Duqu().duqu("lianxi", "denglu00"+i, "password")
        yuqi = Duqu().duqu("lianxi", "denglu00"+i, "yuqi")
        if username==" ":
            username=""
        if password==" ":
            password=""
        Denglu().denglu(username, password)
        #a = Denglu().alert()
        a = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]")
        shiji = a.text
        print shiji
        self.assertIn(yuqi, shiji, msg=u"断言失败")
        pass
    def test_010(self):
        i="10"
        print "test0" + i
        username = Duqu().duqu("lianxi", "denglu0"+i, "username")
        password = Duqu().duqu("lianxi", "denglu0"+i, "password")
        yuqi = Duqu().duqu("lianxi", "denglu0"+i, "yuqi")
        if username==" ":
            username=""
        if password==" ":
            password=""
        Denglu().denglu(username, password)
        #a = Denglu().alert()
        a = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]")
        shiji = a.text
        print shiji
        self.assertIn(yuqi, shiji, msg=u"断言失败")
        pass



if __name__ == '__main__':
    # unittest.main()
    #创建新的测试套件
    nba=unittest.TestSuite()
    #print (nba)
    #添加要执行的测试用例
    # nba.addTest(DENGLU("test_010"))
    # nba.addTest(DENGLU("test_003"))
    # nba.addTest(DENGLU("test_001"))
    # print (nba)
    # 执行已添加测试用例的测试套
    # unittest.TextTestRunner().run(nba)
    # print nba
    #创建一个列表
    list=["test_010","test_003","test_001"]
    for tmp in list:
        nba.addTest(DENGLU(tmp))
        print tmp
    unittest.TextTestRunner().run(nba)







