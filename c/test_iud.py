# -*- coding:utf-8 -*-  
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

conn = MySQLdb.connect(host = '127.0.0.1',
                       port = 3306,
                       user = 'root',
                       passwd = '123456',
                       db = 'pytest',
                       charset = 'utf8' 
                       )

cursor = conn.cursor()

try:
    sql_insert = "insert into user(user,name,age) values('ten','十',10)"
    sql_update = "update user set name = '9' where user = 'nine'"
    sql_delete = "delete from user1 where age < 3"
    
    cursor.execute(sql_insert)
    print(cursor.rowcount)
    cursor.execute(sql_update)
    print(cursor.rowcount)
    cursor.execute(sql_delete)
    print(cursor.rowcount)
    
    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()


cursor.close()
conn.close()