-- 1378. Replace Employee ID With The Unique Identifer
SELECT
  EU.unique_id as unique_id,
  E.name as name
FROM 
  Employees E
  LEFT JOIN EmployeeUNI EU ON E.id = EU.id