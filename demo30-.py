import pymysql
db = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='stu',charset='utf8')
cur = db.cursor()
# sql = "select *from class;"
sql = "select name from class ;"
cur.execute(sql)
# for i in cur:
#     print(i)
all_row = cur.fetchall()
many_row = cur.fetchmany()
one_row = cur.fetchone()
print(all_row)
