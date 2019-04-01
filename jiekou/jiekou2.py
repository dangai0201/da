import pymysql

class Lianjieshujuku(object):
    def __init__(self,host,user,pwd,database):
        self.host=host
        self.user=user
        self.pwd=pwd
        self.database=database
    def lianjieshujuku(self,sql):
        #链接数据库
        self.db=pymysql.connect(self.host,self.user,self.pwd,self.database)
        #使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()
        #执行sql语句
        self.cursor.execute(sql)

        return self.cursor

    def guanbishujuku(self):
        self.db.close()



