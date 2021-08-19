import sqlite3
# 刪除部門

conn = sqlite3.connect('emp.db')
cursor = conn.cursor()

sql = "Delete from departments where dept_id = %d" % (5)
cursor.execute(sql)

conn.commit()
conn.close()

print('Delete OK')
