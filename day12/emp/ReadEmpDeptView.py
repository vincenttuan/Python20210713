import sqlite3
# 請印出 employees 的所有紀錄資料(含欄位名稱)

conn = sqlite3.connect('emp.db')
cursor = conn.cursor()

# Table META-INFO
cursor.execute('PRAGMA TABLE_INFO({})'.format('emp_dept_view'))
names = [header[1] for header in cursor.fetchall()]
for name in names:
    print(name, end='\t')

print('\n------------------------------------------------------------------------')

# 列出 emp_dept_view 紀錄資料
sql = 'SELECT emp_id, dept_id, dept_name, emp_name, emp_salary, create_date ' \
      'FROM emp_dept_view'

cursor.execute(sql)

emps = cursor.fetchall()

for emp in emps:
    print('%6d\t%7d\t%-8s\t%-8s\t%10s\t%s\t' % (emp[0], emp[1], emp[2], emp[3], ('$' + str(emp[4])), emp[5]))
