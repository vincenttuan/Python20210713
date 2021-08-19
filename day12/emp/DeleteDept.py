import sqlite3
# 刪除部門

conn = sqlite3.connect('emp.db')
cursor = conn.cursor()

# 若要刪除 dept_id = 2
# 先確認 employees 有無使用
dept_id = 2
sql = "select count(*) as count from employees where dept_id = %d" % (dept_id)
cursor.execute(sql)
count = cursor.fetchone()
print(count, count[0])
if count[0] == 0:
    sql = "Delete from departments where dept_id = %d" % (dept_id)
    cursor.execute(sql)
    conn.commit()
    print('dept_id:', dept_id, 'Delete OK')
else:
    print('dept_id:', dept_id, '不可刪除')
conn.close()


