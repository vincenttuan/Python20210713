# 建立資料庫
import sqlite3

conn = sqlite3.connect('emp.db')
print(conn)
if conn is not None:
    print('建立/連線成功')
conn.close()

