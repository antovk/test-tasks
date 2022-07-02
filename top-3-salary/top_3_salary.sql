SELECT 
    t1.dept_name as Department
    , t1.emp_name as Employee
    , t1.salary as Salary
FROM
(SELECT 
    emp.name as emp_name
    , emp.salary as salary
    , dept.name as dept_name
    , DENSE_RANK() OVER(partition by emp.departmentId order by emp.salary desc) as dr

FROM 
    EMPLOYEE emp

INNER JOIN 
    DEPARTMENT dept
    ON emp.departmentId = dept.id

ORDER BY
    emp.departmentId asc
    , emp.salary desc) t1
WHERE t1.dr <= 3