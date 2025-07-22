import pymysql
config = {'host': 'ich-db.edu.itcareerhub.de',
 'user': 'ich1',
 'password': 'password',
 }
connection = pymysql.connect(**config)
with connection.cursor() as cursor:
 cursor.execute("SHOW DATABASES")
 for db in cursor:
 print(db)