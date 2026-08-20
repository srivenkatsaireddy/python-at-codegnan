class Employee:
    def __init__(self,emp_id,name,department,salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print(f"Employee ID : {self.emp_id}")
        print(f"Name        : {self.name}")
        print(f"Department  : {self.department}")
        print(f"Salary      : {self.salary}")

    def greet(self):
        print("Welcome ",self.name)

    def update_salary(self,new_salary):
        if new_salary < 0:
            print("Invalid Salary!")
        else:
            self.salary = new_salary
            print("Salary updated successfully.")