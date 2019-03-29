#-*-coding:utf-8-*-
import os,sys
os.getcwd()
sys.path.append(os.getcwd())
import zmail
import time





class Youjian():

    #Zmail仅支持python3，不需要任何外部依赖. 不支持python2
    def sendyoujian(self,subject,content_text,attachments=None):
        #登录账号密码
        #填写是收件人信息
        #添加主题
        a=zmail.server("15712959187@163.com","ylg123456")
        #存放收件人列表
        b=["1195744105@qq.com","1471375117@qq.com"]
        #创建一个空字典
        aa={}
        #主题
        aa['subject']=subject
        #描述
        aa['content_text']=content_text
        #字典内添加附件/最好使用绝对路径
        if attachments!=None :
            aa['attachments']=attachments
        a.send_mail(b,aa)




# Youjian().sendyoujian("优购商城测试邮件","优购商城流程测试","../baogao/2019-03-26 16-34-22.html")