import pymysql
# 打开数据库连接
db = pymysql.connect("localhost","root","12345678","dalian")
print(db)
cursor = db.cursor()
print(cursor)
sql="SELECT * from xuesheng WHERE id=1"
cursor.execute(sql)
results = cursor.fetchall()
for a in results:
    print(a[0],a[1],a[2],a[3])




