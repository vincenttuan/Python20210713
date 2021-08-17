import sqlite3
# 請印出 employees 的所有紀錄資料(含欄位名稱)

conn = sqlite3.connect('emp.db')
cursor = conn.cursor()

# Table META-INFO
cursor.execute('PRAGMA TABLE_INFO({})'.format('employees'))
names = [header[1] for header in cursor.fetchall()]
for name in names:
    print(name, end='\t')

print('\n------------------------------------------------------------')

# 列出 employees 紀錄資料
sql = 'SELECT emp_id, dept_id, emp_name, emp_salary, create_date FROM employees'
cursor.execute(sql)

emps = cursor.fetchall()

for emp in emps:
    print('%6d\t%7d\t%-8s\t%10s\t%s\t' % (emp[0], emp[1], emp[2], ('$' + str(emp[3])), emp[4]))
