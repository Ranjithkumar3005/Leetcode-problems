SELECT 
    e.name AS Employee, 
    e.salary AS Salary, 
    d.name AS Department
FROM 
    employee AS e
JOIN 
    department AS d ON e.departmentId = d.id
WHERE 
    e.salary = (
        SELECT MAX(salary)
        FROM employee
        WHERE departmentId = d.id
    );