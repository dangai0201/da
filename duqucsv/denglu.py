#-*-coding:utf-8-*-
import os,sys
os.getcwd()
sys.path.append(os.getcwd())

import unittest
import time
from fz.fengzhuang import Login
from fz.zhuce import Zhuce
from fz.denglu import Denglu
from duqucsv.huoqucsv import Duqucsv


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
        # for aa in Duqucsv().duqucsv():
        #     b=self.driver.


        pass