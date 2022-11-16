import pymysql
db=pymysql.connect(
                   host='localhost',
                   user='root',
                   password='admin',
                   database='demo2',
                   cursorclass=pymysql.cursors.DictCursor)
cursor=db.cursor()
query="ALTER TABLE student ADD email varchar(100) "
try:
    cursor.execute(query)
    db.commit()
except:
    db.rollback()
db.close()
