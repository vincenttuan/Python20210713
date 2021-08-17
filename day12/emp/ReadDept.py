# 查詢資料
import sqlite3

conn = sqlite3.connect('emp.db')
cursor = conn.cursor()

# 查詢 Table META-INFO
cursor.execute('PRAGMA TABLE_INFO({})'.format('departments'))
headers = cursor.fetchall()
# print(headers)
# ['dept_id', 'dept_name']
names = [header[1] for header in headers]
# print(names)
# 列出欄位名稱
for name in names:
    print(name, end='\t')

print('\n-------------------')

# 多筆查詢 sql 語句
sql = 'SELECT dept_id, dept_name FROM departments'
cursor.execute(sql)
depts = cursor.fetchall()


for dept in depts:
    id   = dept[0]  # dept_id
    name = dept[1]  # dept_name
    print('%-7d\t%-10s\t' % (id, name))


print('-------------------')