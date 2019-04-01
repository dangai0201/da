#-*-coding:utf-8-*-

import unittest
import json
import  requests
from jiekou.fengzhuang import Jiekou,Fanhuizhi


class Testjiekou(unittest.TestCase):
    def setUp(self):
        url = "https://api.edu.3ttech.cn/login/login"
        canshu = {
            'userName': "18410178656",
            'password': "123456",

        }
        fangfa="post"

        self.a=Jiekou(url,fangfa,canshu).panduanfangshi()

        pass
    def tearDown(self):
        pass





    def test_001(self):
        #状态码
        aa=Fanhuizhi(self.a).zhuangtaima()
        self.assertEqual(aa,200)
        print(aa)
        pass

    def test_002(self):
        bb=Fanhuizhi(self.a).zidian()
        self.assertEqual(bb['code'],0)
        pass

    def test_003(self):
        bb=Fanhuizhi(self.a).zidian()
        self.assertEqual(bb['message'],"登录成功")
        pass

    def test_004(self):
        bb=Fanhuizhi(self.a).zidian()
        c=bb['data']
        # 将状态码转换成字符串
        self.assertEqual(str(c['userId']),"600155")
        pass

    def test_005(self):
        bb=Fanhuizhi(self.a).zidian()
        c=bb['data']
        self.assertEqual(c['userName'],"18410178656")
        pass

    def test_006(self):
        bb=Fanhuizhi(self.a).zidian()
        c=bb['data']
        self.assertEqual(c['nickName'],"于力国")
        pass

if __name__ == '__main__':
    unittest.main()