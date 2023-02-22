from demo4_Employee.employee_module import Employee

print(Employee.company_name)
print(Employee.company_location)

Employee.company_name = "einfochips"
Employee.company_location = "Ahmedabad"

print(Employee.company_name)
print(Employee.company_location)

emp1 = Employee()
emp2 = Employee()   # to ask this.
emp3 = Employee()

emp1.emp_id=150
emp1.emp_name="Shubham"
emp1.emp_salary=10000
emp1.emp_performance="A"

emp2.emp_id=151
emp2.emp_name="sakshi"
emp2.emp_salary=11000
emp2.emp_performance="A"

emp3.emp_id=152
emp3.emp_name="Bunny"
emp3.emp_salary=12000
emp3.emp_performance="A"


print(emp1.emp_id)
print(emp2.emp_id)
print(emp3.emp_id)
#employee-1
print(emp1.emp_id)
print(emp1.emp_name)
print(emp1.emp_salary)
print(emp1.emp_performance)
#employee-2
print(emp2.emp_id)
print(emp2.emp_name)
print(emp2.emp_salary)
print(emp2.emp_performance)
#employee-3
print(emp3.emp_id)
print(emp3.emp_name)
print(emp3.emp_salary)
print(emp3.emp_performance)