import json
from employees import Address
from employees import Employee



address = Address("42 Wallaby Way", "Sydney")
employee = Employee("P. Sherman", address)

emp_dict = employee.to_dict()
with open("employee.json", "w") as file:
    json.dump(emp_dict, file, indent=4)