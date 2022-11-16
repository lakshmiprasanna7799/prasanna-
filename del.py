import pymysql
db=pymysql.connect(
                   host='localhost',
                   user='root',
                   password='admin',
                   database='demo2',
                   cursorclass=pymysql.cursors.DictCursor)
cursor=db.cursor()
query="delete from student where age>32"
try:
    cursor.execute(query)
    db.commit()
except:
    db.rollback()
db.close()