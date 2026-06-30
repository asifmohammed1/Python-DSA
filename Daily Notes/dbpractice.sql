--Reports (DA)

--Total Employees
SELECT COUNT(*) as TotalEmp from Employees

--Average Salary
SELECT AVG(Salary) as Averagesal from Employees

--Department wise employees count
SELECT d.dept_name, count(e.emp_id) as Numberofemp from Department d
left join employees e
on d.dept_id = e.dept_id
group by d.dept_name

--Department wise avg salary
SELECT d.dept_name, AVG(e.salary) as AvgSalary from Department d
left join employees e
on d.dept_id = e.dept_id
group by d.dept_name

--Highest paid employees
SELECT * from employees
order by salary desc
limit 1

--employees without projects
SELECT e.emp_name from employees e
left join projects p
on e.emp_id = p.emp_id
WHERE p.project_id is null

--projects: emp_id, budget, project_name

--Total budget by department
--Department, Employees, Projects
SELECT d.dept_name, sum(p.budget) as TotalBudget from department d
left join employees e
on d.dept_id = e.dept_id
left join projects p
on e.emp_id = p.emp_id
group by d.dept_name

