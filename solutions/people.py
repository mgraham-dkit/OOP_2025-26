class Person:
    def __init__(self, first, last, age, left_handed):
        self.first = first
        self.last = last
        self.age = age
        self.left_handed = left_handed

    def display(self):
        if self.left_handed:
            print(f"{self.first} {self.last}")
        else:
            print(f"{self.first.upper()} {self.last.upper()}")


class Employee:
    def __init__(self, staff_id, first="John", last="Doe", title="Entry-level", salary=25000):
        self.staff_id = staff_id
        self.first = first
        self.last = last
        self.title = title
        self._salary = salary

    def get_salary(self):
        return self._salary

    def display(self):
        print(f"Employee[id: {self.staff_id}, first name: {self.first}, last name = {self.last}, salary = €{self._salary}]")

    def calc_net_pay(self):
        yearly_tax = self._salary * 0.42
        net_yearly_salary = self._salary - yearly_tax
        monthly_pay = net_yearly_salary/12
        return monthly_pay

    def calc_monthly_pay(self):
        return (self._salary * 0.58) / 12

    def calc_bonus(self):
        if "manager" in self.title.lower():
            return self._salary * 0.15
        elif "intern" in self.title.lower():
            return self._salary * 0.02
        elif "tech lead" in self.title.lower():
            return self._salary * 0.10
        else:
            return self._salary * 0.06


