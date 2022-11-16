import pymysql
db=pymysql.connect(
                   host='localhost',
                   user='root',
                   password='admin',
                   database='demo1',
                   cursorclass=pymysql.cursors.DictCursor)
with connection.cursor() as cursor:
    sql ="select * from student"
    cursor.execute(sql)
    result=cursor.fetchone()
    print(result)
#cursor=db.cursor()
#query='insert into student values("john","dell",24,"248")'
#cursor.execute("SELECT VERSION()")
#data=cursor.fetchone()
#print("Database version: %s" %data)
#try:
      #  cursor.execute(query)
       # db.commit()
#except:
        #db.rollback()
#db.close()