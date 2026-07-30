-- Create Tables

CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50),
    location VARCHAR(50));

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    salary DECIMAL(10,2),
    joining_date DATE,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id));

CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100),
    budget DECIMAL(12,2),
    emp_id INT,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id));

-- Insert Departments

INSERT INTO departments VALUES
(1,'HR','Hyderabad'),
(2,'IT','Bangalore'),
(3,'Finance','Mumbai'),
(4,'Sales','Chennai');

-- Insert Employees

INSERT INTO employees VALUES
(101,'Rahul',28,'Male',55000,'2022-03-10',2),
(102,'Priya',30,'Female',72000,'2021-07-15',1),
(103,'Amit',35,'Male',68000,'2020-01-20',2),
(104,'Sneha',27,'Female',50000,'2023-05-12',4),
(105,'Karan',31,'Male',75000,'2019-09-08',3),
(106,'Anjali',26,'Female',62000,'2022-11-11',2),
(107,'Vikram',29,'Male',58000,'2021-04-25',4);

-- Insert Projects

INSERT INTO projects VALUES
(201,'Website Development',200000,101),
(202,'Payroll System',150000,102),
(203,'Banking Software',300000,103),
(204,'Marketing Campaign',120000,104),
(205,'Finance Dashboard',250000,105);

-- Question 1
SELECT emp_name, salary, dept_id
FROM employees;

-- Question 2
SELECT *
FROM employees
WHERE salary > 60000;

-- Question 3
UPDATE employees
SET salary = salary + 5000
WHERE emp_id = 101;

SELECT *
FROM employees
WHERE emp_id = 101;

-- Question 4
SELECT e.emp_name, d.dept_name, p.project_name
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id
INNER JOIN projects p
ON e.emp_id = p.emp_id;

-- Question 5
SELECT d.dept_name, COUNT(e.emp_id) AS total_employees
FROM departments d
LEFT JOIN employees e
ON d.dept_id = e.dept_id
GROUP BY d.dept_name;

-- Bonus
ALTER TABLE employees
ADD COLUMN email VARCHAR(100);

DELETE FROM employees
WHERE emp_id = 107;

TRUNCATE TABLE projects;

DROP TABLE projects;

ALTER TABLE employees
RENAME TO employee_details;