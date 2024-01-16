export default function createEmployeesObject(departmentName, employees) {
  const employee = {};
  employee[departmentName] = employees;
  return employee;
}
