# application.py

class CareerApplication:

    def __init__(self, application_id, company_name, role, location, status):
        self.__application_id = application_id
        self.__company_name = company_name
        self.__role = role
        self.__location = location
        self.__status = status


    def get_application_id(self):
        return self.__application_id

    def get_company_name(self):
        return self.__company_name

    def get_role(self):
        return self.__role

    def get_location(self):
        return self.__location

    def get_status(self):
        return self.__status


    def set_company_name(self, company_name):
        self.__company_name = company_name

    def set_role(self, role):
        self.__role = role

    def set_location(self, location):
        self.__location = location

    def set_status(self, status):
        self.__status = status


    def display(self):
        print(f"Application ID : {self.__application_id}")
        print(f"Company Name   : {self.__company_name}")
        print(f"Role           : {self.__role}")
        print(f"Location       : {self.__location}")
        print(f"Status         : {self.__status}")