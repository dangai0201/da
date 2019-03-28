#-*-coding:utf-8-*-
import  unittest
from fz.fengzhuang import Login
from fz.zhuce import Zhuce
from fz.denglu import Denglu
from duquxml.huoquxml import Duqu

from mokuai.zhuce import ZHUCE
from mokuai.denglu import DENGLU

class Loginzhuce():
    def test_001(self):
        # 1.创建一个空的测试套件
        # 2.添加测试用例
        # 3.执行测试套件
        nba = unittest.TestSuite()
        print nba
        #执行该模块下方001用例
        nba.addTest(ZHUCE("test_003"))
        #print nba
        #执行该模块下方的所有用例
        #nba.addTest(unittest.makeSuite(ZHUCE))
        unittest.TextTestRunner().run(nba)
        pass
    def test_002(self):
        nba = unittest.TestSuite()
        nba.addTest(DENGLU("test_002"))
        unittest.TextTestRunner().run(nba)

if __name__ == '__main__':
   Loginzhuce().test_001()



