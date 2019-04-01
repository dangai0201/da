import requests

class Jiekou(object):
    def __init__(self,url,fangfa,canshu):
        self.url=url
        self.canshu=canshu
        self.fangfa=fangfa
    def panduanfangshi(self):
        if self.fangfa.lower()=="get":
            a=requests.get(self.url,params=self.canshu)
            return a

        elif self.fangfa.lower()=="post":
            b=requests.post(self.url,data=self.canshu)
            return b
        else:
            return False


class Fanhuizhi(object):
    def __init__(self,fanhuizhi):
        self.fanhuizhi=fanhuizhi

    def zidian(self):
        zidian=self.fanhuizhi.json()
        return zidian

    def zhuangtaima(self):
        zhuangtaima = self.fanhuizhi.status_code
        return zhuangtaima


