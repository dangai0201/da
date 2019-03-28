#-*-coding:utf-8-*-

import unittest
import time
from fz.fengzhuang import Login
from fz.zhuce import Zhuce
from fz.denglu import Denglu
from duquexcl.huoquexel import Huoquexel

time1=time.strftime("%Y/%m/%d %H:%M:%S",time.localtime())

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
        i="2"
        username = Huoquexel().duquexel("C"+i)
        password = Huoquexel().duquexel("D"+i)
        yuqi = Huoquexel().duquexel("E"+i)
        #判断是否有空
        if username == " ":
            username=""
        if password==" ":
            password=""
        Denglu().denglu(username, password)
        a = Denglu().alert()
        #a = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]")
        shiji = a.text
        print (shiji)
        Huoquexel().xieruexel("F"+i,shiji)
        Huoquexel().xieruexel("H"+i,time1)
        self.assertIn(yuqi, shiji, msg=u"断言失败")
        pass
    def test_002(self):
        i="3"
        username = Huoquexel().duquexel("C"+i)
        password = Huoquexel().duquexel("D"+i)
        yuqi = Huoquexel().duquexel("E"+i)
        if username == " ":
            username=""
        if password==" ":
            password=""
        Denglu().denglu(username, password)
        a = Denglu().alert()
        #a = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]")
        shiji = a.text
        print (shiji)
        Huoquexel().xieruexel("F" + i, shiji)
        Huoquexel().xieruexel("H" + i, time1)
        self.assertIn(yuqi, shiji, msg=u"断言失败")
        pass
    def test_003(self):
        i="4"
        username = Huoquexel().duquexel("C"+i)
        password = Huoquexel().duquexel("D"+i)
        yuqi = Huoquexel().duquexel("E"+i)
        Denglu().denglu(username, password)
        #a = Denglu().alert()
        a = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]")
        shiji = a.text
        print (shiji)
        Huoquexel().xieruexel("F" + i, shiji)
        Huoquexel().xieruexel("H" + i, time1)
        self.assertIn(yuqi, shiji, msg=u"断言失败")
        pass
    def test_004(self):
        i="5"
        username = Huoquexel().duquexel("C"+i)
        password = Huoquexel().duquexel("D"+i)
        yuqi = Huoquexel().duquexel("E"+i)
        Denglu().denglu(username, password)
        #a = Denglu().alert()
        a = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]")
        shiji = a.text
        print (shiji)
        Huoquexel().xieruexel("F" + i, shiji)
        Huoquexel().xieruexel("H" + i, time1)
        self.assertIn(yuqi, shiji, msg=u"断言失败")
        pass

    def test_005(self):
        i="6"
        username = Huoquexel().duquexel("C"+i)
        password = Huoquexel().duquexel("D"+i)
        yuqi = Huoquexel().duquexel("E"+i)
        Denglu().denglu(username, password)
        #a = Denglu().alert()
        a = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]")
        shiji = a.text
        print (shiji)
        Huoquexel().xieruexel("F" + i, shiji)
        Huoquexel().xieruexel("H" + i, time1)
        self.assertIn(yuqi, shiji, msg=u"断言失败")
        pass

if __name__ == '__main__':
    unittest.main()