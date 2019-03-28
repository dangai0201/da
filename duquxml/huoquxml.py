#-*-coding:utf-8-*-
from xml.dom import minidom
#读取.xml文档
class Duqu():
    def duqu(self,filename,one,two):
        #打开xml文档
        #a=minidom.parse('duquxml/lianxi.xml')

        a=minidom.parse("../duquxml/"+filename+".xml")
        #b=a.getElementsByTagName("denglu003")[0]
        b=a.getElementsByTagName(one)[0]

        #c=b.getElementsByTagName("password")[0].childNodes[0].nodeValue

        c=b.getElementsByTagName(two)[0].childNodes[0].nodeValue


        return c

# a=Duqu().duqu()
# print a
