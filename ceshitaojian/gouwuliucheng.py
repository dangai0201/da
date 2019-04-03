#-*-coding:utf-8-*-
import os,sys
os.getcwd()
sys.path.append(os.getcwd())
import  unittest
from fz.fengzhuang import Login
from fz.zhuce import Zhuce
from fz.denglu import Denglu
from duquxml.huoquxml import Duqu

from mokuai.zhuce import ZHUCE
from mokuai.denglu import DENGLU
from mokuai.liucheng import Liucheng
from baogao.baogao import Baogao
from youjian.youjian import Youjian
from youjian.youjian2 import Youjian
import time
from baogao.jietu.jietu import Jietu





class Gouwuliucheng():
    def test_001(self):
        time1=time.strftime("%Y-%m-%d %H-%M", time.localtime())
        # 1.创建一个空的测试套件
        # 2.添加测试用例
        # 3.执行测试套件
        nba = unittest.TestSuite()
        #print nba
        #执行该模块下方001用例
        nba.addTest(DENGLU("test_018"))
        nba.addTest(Liucheng("test_001"))
        #print nba
        #执行该模块下方的所有用例
        #nba.addTest(unittest.makeSuite(ZHUCE))
        #unittest.TextTestRunner().run(nba)


        Baogao().getbaogao(u"",u"ecshop",u"购物流程用例",nba)
        #filename = "baogao/" + time1 + ".html"
        #filename = "../baogao/" + time1 + ".html"
        #Youjian().sendyoujian("优购商城", "优购商城流程测试", filename)
        Youjian.sendEmail("大连必胜","优购商城流程测试")

        pass



if __name__ == '__main__':
    Gouwuliucheng().test_001()
