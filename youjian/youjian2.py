#-*-coding:utf-8-*-
import zmail
import time






class Youjian():
    def sendEmail(self,subject=None, content=None,attachments=None):
        '''
        1,登录发件人的邮箱账号和授权码非登录密码
        2，填写收件人信息
        3，主题及附件以及正文内容
        :return:
        '''
        time1 = time.strftime("%Y-%m-%d ", time.localtime())
        server = zmail.server("15712959187@163.com", "ylg123456")
        #存放要发送的收件人列表
        recive = "1471375117@qq.com"
        #创建一个空字典
        dict1 = {}
        #在字典内添加主题
        dict1["subject"] = subject
        #字典内添加内容
        dict1["content_text"] =content
        #字典内添加附件/最好使用绝对路径

        b = []
        dict1["attachments"] = b
        # aaa="../baogao/jietu/jietu.png"
        aaa= "../baogao/jietu/"+time1+".png"
        print(aaa)
        # aaa="baogao/jietu/jietu.png"
        aaa1="../baogao/"+time1+".html"
        print(aaa1)
        # aaa1="../baogao/2019-04-08 10-29.html"




        # if HTML !=None:
        #     if type(HTML) == list:
        #         for html in HTML:
        #             b.append( "baogao/" + html + ".png")
        #     else:
        #         b.append("baogao/" + HTML + ".png")
        # if PNG !=None:
        #     if type(PNG) == list:
        #         for png in PNG:
        #                 b.append("../baogao/jietu/"+png+".png")
        #     else:
        #         b.append("../baogao/jietu/" + PNG + ".png")
        # b.append(aaa)
        # b.append(aaa1)
        if aaa1 and aaa!=None:
            b.append(aaa1)
            b.append(aaa)
        else:
            print("请添加路径")


        server.send_mail(recive, dict1)
# Youjian().sendEmail("大连必胜","优购商城流程测试")




