import sqlite3
# 修改部門

conn = sqlite3.connect('emp.db')
cursor = conn.cursor()

sql = "Update departments set dept_name='%s' where dept_id=%d" % ('Financial', 5)
cursor.execute(sql)

conn.commit()
conn.close()

print('Update ok')