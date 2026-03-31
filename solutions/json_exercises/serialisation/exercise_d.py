import json
from employees import Address
from employees import Employee


emp_list = []
for i in range(3):
    address = Address(f"{i} Wallaby Way", f"Syd{i}ney")
    employee = Employee(f"P. {i} Sherman", address)
    emp_list.append(employee)

emp_dicts = [emp.to_dict() for emp in emp_list]

with open("employees.json", "w") as file:
    json.dump(emp_dicts, file, indent=4)