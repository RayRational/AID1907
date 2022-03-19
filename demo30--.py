import pymysql
db = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='stu',charset='utf8')
cur = db.cursor()
id = input("id:")
name = input("Name:")
age = input('Age:')
sex = input("sex:")
tel = input("tel:")
score = input("score:")
try:
   # sql = "insert into class values (%s,'%s',%s,'%s',%s,%s)"%(id,name,age,sex,tel,score)
   sql = "insert into class values (%s,%s,%s,%s,%s,%s);"
   cur.execute(sql,[id,name,age,sex,tel,score])
   db.commit()
except Exception as e:
    print(e)
    db.rollback()
cur.close()
db.close()