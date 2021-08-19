import sqlite3
# 建立一個 financial 財務部門

conn = sqlite3.connect('emp.db')
cursor = conn.cursor()

sql = "Insert into departments(dept_name) values ('%s')" % ('financial')

cursor.execute(sql)
print("dept_id:", cursor.lastrowid)
conn.commit()
conn.close()