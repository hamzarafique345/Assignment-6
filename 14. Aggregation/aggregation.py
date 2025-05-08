# Assignment 14:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference
# to an Employee object that exists independently of it.


class Employee:
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return f"Employee: {self.name}"

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  

    def show_department_info(self):
        return f"Department: {self.dept_name}, {self.employee.get_details()}"


emp1 = Employee("Hamza")


dept1 = Department("IT", emp1)

print(dept1.show_department_info())

