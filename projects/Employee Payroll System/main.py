from employee import Employee

employees = []

while True:
    print("\n========= Employee Payroll System =========")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Update Salary")
    print("4. Search Employee")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        salary = int(input("Enter your salary: "))

        employee = Employee(emp_id,name,department,salary)
        employees.append(employee)
        print("Employee Added Successfully")

    elif choice == 2:
        print("Display Selected")

    elif choice == 3:
        print("Update Salary Selected")

    elif choice == 4:
        print("Search Employee Selected")

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid Choice")


# step 11