#-*-coding:utf-8-*-
from xml.dom import minidom
#读取.xml文档
class Duqu():
    def duqu(self):
        #打开xml文档
        a=minidom.parse('duquxml/lianxi.xml')

        b=a.getElementsByTagName("denglu001")[0]

        #c=b.getElementsByTagName("password")[0].childNodes[0].nodeValue

        c=b.getElementsByTagName("password")[0].childNodes[0].nodeValue


        return c

a=Duqu().duqu()
print (a)
