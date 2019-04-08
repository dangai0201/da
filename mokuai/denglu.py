# -*-coding:utf-8-*-
import os,sys
os.getcwd()
sys.path.append(os.getcwd())
import time
import unittest

from fz.fengzhuang import Login
from fz.zhuce import Zhuce
from fz.denglu import Denglu




class DENGLU(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = Login().driver
        pass

    @classmethod
    def tearDownClass(self):
        #Denglu().guanbi()
        pass

    def setUp(self):


        pass

    def tearDown(self):
        # 通过try进行判断有没有弹框
        # try:
        #     Denglu().alert().accept()
        # except Exception:
        #     #print u"没有弹框"
        #     pass
        # self.driver.find_element_by_xpath("//*[@id=\"ECS_MEMBERZONE\"]/a[2]").click()
        pass

    # def test_001(self):
    #
    #     Denglu().denglu("", "")
    #     a = Denglu().alert()
    #     shiji = a.text
    #     # print (shiji)
    #     yuqi = u"用户名不能为空"
    #     self.assertIn(yuqi, shiji, msg=u"断言失败")
    #     Denglu().alert().accept()
    #
    #     pass
    #
    # def test_002(self):
    #     Denglu().denglu("123456", "")
    #     a = Denglu().alert()
    #     shiji = a.text
    #     # print (shiji)
    #     yuqi = u"登录密码不能为空"
    #     self.assertIn(yuqi, shiji, msg=u"断言失败")
    #     Denglu().alert().accept()
    #     pass
    #
    # def test_003(self):
    #     Denglu().denglu("123456", "123123123")
    #     shiji = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]").text
    #     print (shiji)
    #     yuqi = u"用户名或密码错误"
    #     self.assertEqual(yuqi, shiji)
    #
    #     pass
    #
    # # 长度空
    # def test_005(self):
    #     Denglu().denglu(" ", "123456")
    #     shiji = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]").text
    #     print (shiji)
    #     yuqi = u"用户名或密码错误"
    #     self.assertEqual(yuqi, shiji)
    #     pass
    #
    # # 长度3
    # def test_006(self):
    #     Denglu().denglu("988", "123456")
    #     shiji = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]").text
    #     print (shiji)
    #     yuqi = u"用户名或密码错误"
    #     self.assertEqual(yuqi, shiji)
    #     pass
    #
    # # 长度14
    # def test_007(self):
    #     Denglu().denglu("12345678912345", "123456")
    #     shiji = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]").text
    #     print (shiji)
    #     yuqi = u"用户名或密码错误"
    #     self.assertEqual(yuqi, shiji)
    #     pass
    #
    # # 长度2
    # def test_008(self):
    #     Denglu().denglu("12", "123456")
    #     shiji = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]").text
    #     print (shiji)
    #     yuqi = u"用户名或密码错误"
    #     self.assertEqual(yuqi, shiji)
    #     pass
    #
    # # 长度15
    # def test_009(self):
    #     Denglu().denglu("123456789123456", "123456")
    #     shiji = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]").text
    #     print (shiji)
    #     yuqi = u"用户名或密码错误"
    #     self.assertEqual(yuqi, shiji)
    #     pass
    #
    # # 类型：汉字
    # def test_010(self):
    #     Denglu().denglu(u"你好", "123456")
    #     shiji = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]").text
    #     print (shiji)
    #     yuqi = u"用户名或密码错误"
    #     self.assertEqual(yuqi, shiji)
    #     pass
    #
    # # 类型：字母
    # def test_0011(self):
    #     Denglu().denglu("abd", "123456")
    #     shiji = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]").text
    #     print (shiji)
    #     yuqi = u"用户名或密码错误"
    #     self.assertEqual(yuqi, shiji)
    #     pass
    #
    # # 类型：数字
    # # 类型：特殊字符
    # def test_012(self):
    #     Denglu().denglu(u"？？？？", "123456")
    #     shiji = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]").text
    #     print (shiji)
    #     yuqi = u"用户名或密码错误"
    #     self.assertEqual(yuqi, shiji)
    #     pass
    #
    # # #组合
    # # 大小写
    # def test_013(self):
    #     Denglu().denglu("abcASSS", "123456")
    #     shiji = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]").text
    #     print (shiji)
    #     yuqi = u"用户名或密码错误"
    #     self.assertEqual(yuqi, shiji)
    #     pass
    #
    # # 空格
    # def test_014(self):
    #     Denglu().denglu("abcASS S", "123456")
    #     shiji = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]").text
    #     print (shiji)
    #     yuqi = u"用户名或密码错误"
    #     self.assertEqual(yuqi, shiji)
    #     pass
    #
    # # 密码长度
    # # 前中后去空格别的同用户名输入框
    # # 前空格
    # def test_015(self):
    #     Denglu().denglu("  abcASSS", "123456")
    #     shiji = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]").text
    #     print (shiji)
    #     yuqi = u"用户名或密码错误"
    #     self.assertEqual(yuqi, shiji)
    #     pass
    #
    # # 中空格
    # def test_016(self):
    #     Denglu().denglu("abc ASSS", "123456")
    #     shiji = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]").text
    #     print (shiji)
    #     yuqi = u"用户名或密码错误"
    #     self.assertEqual(yuqi, shiji)
    #     pass
    #
    # # 后空格
    # def test_017(self):
    #     Denglu().denglu("abcASSS    ", "123456")
    #     try:
    #         a=Denglu().alert()
    #     except Exception:
    #         a=self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]")
    #     #return后代码不会向下执行
    #     #return a
    #     shiji=a.text
    #     print (shiji)
    #     yuqi = u"用户名或密码错误"
    #     self.assertEqual(yuqi, shiji)
    #     pass
    #
    # def test_004(self):
    #     Denglu().denglu("123456", "123456")
    #     shiji = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[1]").text
    #     print (shiji)
    #     yuqi = u"登录成功"
    #     self.assertEqual(yuqi, shiji)
    #     # self.driver.find_element_by_xpath("//*[@id=\"ECS_MEMBERZONE\"]/a[2]").click()
    #     pass
    def test_018(self):
        Denglu().denglu("123456", "123456")
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/p[2]/a").click()



if __name__ == '__main__':
    unittest.main()
