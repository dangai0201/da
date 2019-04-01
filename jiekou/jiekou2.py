#-*-coding:utf-8-*-

import unittest
import json
import  requests
from jiekou.fengzhuang import Jiekou,Fanhuizhi
from jiekou.jiekouxml import Duqu


class Testjiekou(unittest.TestCase):
    def setUp(self):
        url = "https://api.edu.3ttech.cn/login/login"
        b=Duqu().duqu("jie","jiekou001","password")
        a=Duqu().duqu("jie","jiekou001","username")
        canshu = {
            'userName': a,
            'password': b,

        }
        fangfa="post"

        self.a=Jiekou(url,fangfa,canshu).panduanfangshi()

        pass
    def tearDown(self):
        pass





    def test_001(self):
        #状态码
        aa=Fanhuizhi(self.a).zidian()
        print(aa)



if __name__ == '__main__':
    unittest.main()