from application import CareerApplication


class CareerTracker:

    def __init__(self):
        self.applications = []

    def add_application(self):

        print("\nAdd Career Application")

        application_id = int(input("Enter Application ID : "))
        company_name = input("Enter Company Name    : ")
        role = input("Enter Role            : ")
        location = input("Enter Location        : ")
        status = input("Enter Status          : ")

        application = CareerApplication(
            application_id,
            company_name,
            role,
            location,
            status
        )

        self.applications.append(application)

        print("\nApplication Added Successfully!")

    def view_applications(self):

        print("\nCareer Applications")

        if len(self.applications) == 0:
            print("No Applications Found.")
            return

        for application in self.applications:
            application.display()

    def search_application(self):

        company_name = input("\nEnter Company Name : ")

        for application in self.applications:

            if application.get_company_name().lower() == company_name.lower():
                application.display()
                break

        else:
            print("Application Not Found.")

    def update_status(self):

        application_id = int(input("\nEnter Application ID : "))

        for application in self.applications:

            if application.get_application_id() == application_id:

                print("Current Status :", application.get_status())

                new_status = input("Enter New Status : ")

                application.set_status(new_status)

                print("Status Updated Successfully.")
                break

        else:
            print("Application Not Found.")

    def delete_application(self):

        application_id = int(input("\nEnter Application ID : "))

        for application in self.applications:

            if application.get_application_id() == application_id:

                self.applications.remove(application)

                print("Application Deleted Successfully.")
                break

        else:
            print("Application Not Found.")