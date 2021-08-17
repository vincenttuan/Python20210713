-- 建立 View
CREATE VIEW emp_dept_view
AS
SELECT
	e.emp_id, e.dept_id, d.dept_name, e.emp_name, e.emp_salary, e.create_date
FROM
	employees e, departments d
WHERE
	e.dept_id = d.dept_id;

-- 查詢 View
SELECT
    emp_id, dept_id, dept_name, emp_name, emp_salary, create_date
FROM
    emp_dept_view

