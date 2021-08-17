# 查詢資料
import sqlite3

conn = sqlite3.connect('emp.db')
cursor = conn.cursor()

# 多筆查詢 sql 語句
sql = 'SELECT dept_id, dept_name FROM departments'
cursor.execute(sql)
depts = cursor.fetchall()

for dept in depts:
    id   = dept[0]  # dept_id
    name = dept[1]  # dept_name
    print('%d\t%s\t' % (id, name))


