select d.name as Department , e.name as Employee , e.salary as Salary
from Employee e
inner join Department d on e.departmentId = d.id
where e.salary = (select max(salary) FROM Employee WHERE d.id = Employee.departmentId);