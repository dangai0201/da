# -*-coding:utf-8-*-
import os,sys
os.getcwd()
sys.path.append(os.getcwd())

import unittest
import time
from fz.fengzhuang import Login
from fz.zhuce import Zhuce
from fz.denglu import Denglu


from fz.sousuo import Sousuo
from fz.sousuojieguo import Sousuojieguo
from fz.shangpinxiangqing import Shangpinxiangqing
from fz.gouwuche import Gouwuche
from fz.tijiaodingdan import Tijiaodingdan
from fz.gerenxinxi import Genrenxinxi
import os,sys
os.getcwd()
sys.path.append(os.getcwd())


class Liucheng(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = Login().driver
        pass

    @classmethod
    def tearDownClass(self):
      #  Denglu().guanbi()
        pass

    def setUp(self):


        pass

    def tearDown(self):
        #通过try进行判断有没有弹框
        # try:
        #     Denglu().alert().accept()
        # except Exception:
        #     #print u"没有弹框"
        #     pass
        # self.driver.find_element_by_xpath("//*[@id=\"ECS_MEMBERZONE\"]/a[2]").click()
        pass

    def test_001(self):
        Sousuo().sousuo(u"戒指")
        Sousuojieguo().sousuojieguo(2)
        Shangpinxiangqing().shangpinxiangqing(2)

        Gouwuche().dianjijiesuan()
        Tijiaodingdan().tijiaodingdan()
        yuqi=Tijiaodingdan().dingdanhao()
        print (yuqi)

        time.sleep(3)
        Genrenxinxi().gerenxinxi()
        shiji=Genrenxinxi().zuixindingdan()
        print (shiji)
        self.assertEqual(yuqi,shiji)




        pass
