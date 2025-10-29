from tools.employee_validator import *


class Employee:
    def __init__(self, employee_id, first_name, last_name, salary, occupation, phone_number, username, password, role):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.occupation = occupation
        self.phone_number = phone_number
        self.username = username
        self.password = password
        self.role = role

    def validate(self):
        first_name_validator(self.first_name)
        last_name_validator(self.last_name)
        salary_validator(self.salary)
        occupation_validator(self.occupation)
        phone_number_validator(self.phone_number)
        username_validator(self.username)
        password_validator(self.password)
        role_validator(self.role)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
     return f"{self.__dict__}"


    def to_tuple(self):
      return tuple(
        (self.employee_id, self.first_name, self.last_name, self.salary, self.occupation, self.phone_number, self.username,
         self.password,self.role))
