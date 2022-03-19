import pymysql
db = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='stu',charset='utf8')
cur = db.cursor()
sql = "insert into class values (1,'Ray',20,'m',110,79);"
cur.execute(sql)
db.commit()
cur.close()
db.close()