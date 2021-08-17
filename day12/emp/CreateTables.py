import sqlite3
'''
建立資料表
1. 部門 departments
+---------+-----------+
| dept_id | dept_name |
+---------+-----------+
| INTEGER | VARCHAR   |
+---------+-----------+
|   PK    | NOT NULL  |
+---------+-----------+

2. 員工 employees
+--------+---------+----------+------------+-------------+
| emp_id | dept_id | emp_name | emp_salary | create_date |
+--------+---------+----------+------------+-------------+
| INTEGER| INTEGER | VARCHAR  |  INTEGER   |  TIMESTAMP  |
+--------+---------+----------+------------+-------------+
|   PK   |   FK    | NOT NULL |            |   DEFAULT   |
+--------+---------+----------+------------+-------------+

'''

create_departments_sql = '''
    CREATE TABLE departments(
        dept_id INTEGER PRIMARY KEY AUTOINCREMENT,
        dept_name VARCHAR NOT NULL
    );
'''

create_employees_sql = '''
    CREATE TABLE employees(
        emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
        dept_id INTEGER,
        emp_name VARCHAR NOT NULL,
        emp_salary INTEGER,
        create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        CONSTRAINT fk_departments FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
    );
'''

# 建立資料表
conn = sqlite3.connect('emp.db')
cursor = conn.cursor()
cursor.execute(create_departments_sql)
cursor.execute(create_employees_sql)
conn.commit()
print('Table 建立完成')
conn.close()



