# Select - read the data from table
# Create - Create a table
# Alter - Update the table structure (columns)
# Drop - Delete the full table
# Rename - Rename the table

# Insert - Add the rows in table
# Update - Update the data (rows)
# Delete - Delete the row
# Where - Filter the rows
# Truncate - Delete all the rows

# A LEFT JOIN returns:
# All records from the left table
# Matching records from the right table
# If there is no match, the right table values become NULL

# A RIGHT JOIN returns:
# All records from the right table
# Matching records from the left table
# If there is no match, the left table values become NULL

select c.first_name, o.item
from orders o
left join customers c
on c.customer_id = o.customer_id

--(orders is left table and customer is right table)
--either you change the position of table or left to right (it change to right join)


-- 1. CREATE DATABASE - Creates a new database.
CREATE DATABASE company_db;

-- 2. CREATE TABLE - Creates a new table.
CREATE TABLE employees (
    emp_id INT,
    emp_name VARCHAR(50),
    salary INT
);

-- 3. INSERT - Adds new records into a table.
INSERT INTO employees VALUES (101, 'Asif', 60000);

-- 4. SELECT - Retrieves data from a table.
SELECT * FROM employees;

-- 5. WHERE - Filters rows based on a condition.
SELECT * FROM employees WHERE salary > 50000;

-- 6. UPDATE - Modifies existing records.
UPDATE employees
SET salary = 65000
WHERE emp_id = 101;

-- 7. DELETE - Removes records from a table.
DELETE FROM employees
WHERE emp_id = 101;

-- 8. ALTER TABLE - Changes the table structure.
ALTER TABLE employees
ADD age INT;

-- 9. DROP COLUMN - Removes a column from a table.
ALTER TABLE employees
DROP COLUMN age;

-- 10. RENAME COLUMN - Renames a column.
ALTER TABLE employees
RENAME COLUMN emp_name TO employee_name;

-- 11. TRUNCATE - Removes all rows but keeps the table.
TRUNCATE TABLE employees;

-- 12. DROP TABLE - Deletes the table permanently.
DROP TABLE employees;