from model import Employee
from service import EmployeeService
from tools.logging import Logger


class EmployeeController:
    @classmethod
    def save(cls, first_name, last_name, salary, occupation, phone_number, username, password, role):
        try:
            employee = Employee(None, first_name, last_name, salary, occupation, phone_number, username, password, role)
            employee.validate()
            employee = EmployeeService.save(employee)
            Logger.info(f"Employee {employee} saved")
            return True, f"Employee Saved Successfully"
        except Exception as e:
            Logger.error(f"Employee Save Error: {e}")
            return False, e

    @classmethod
    def update(cls, employee_id, first_name, last_name, salary, occupation, phone_number, username, password, role):
        try:
            employee = Employee(employee_id, first_name, last_name, salary, occupation, phone_number, username,
                                password, role)
            employee.validate()
            employee = EmployeeService.update(employee)
            Logger.info(f"Employee {employee} updated")
            return True, "Employee Updated Successfully"
        except Exception as e:
            Logger.error(f"Employee Update Error: {e}")
            return False, e

    @classmethod
    def delete(cls, employee_id):
        try:
            employee = EmployeeService.delete(employee_id)
            Logger.info(f"Employee {employee} deleted")
            return True, f"Employee Deleted Successfully"
        except Exception as e:
            Logger.error(f"Employee Delete Error: {e}")
            return False, e

    @classmethod
    def find_all(cls):
        try:
            employee_list = EmployeeService.find_all()
            Logger.info("Employee FindAll")
            return True, employee_list
        except Exception as e:
            Logger.error(f"Employee FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, employee_id):
        try:
            employee = EmployeeService.find_by_id(employee_id)
            Logger.info(f"Employee FindById {employee_id}")
            return True, employee
        except Exception as e:
            Logger.error(f"{e} With Id {employee_id}")
            return False, e

    @classmethod
    def find_by_firstname_and_lastname(cls, firstname, lastname):
        try:
            employee_list = EmployeeService.find_by_firstname_and_lastname(firstname, lastname)
            Logger.info(f"Employee FindByFirstnameAndLastname {firstname} {lastname}")
            return True, employee_list
        except Exception as e:
            Logger.error(f"Employee FindByFirstnameAndLastname Error: {e}")
            return False, e

    @classmethod
    def find_by_phone_number(cls, phone_number):
        try:
            employee_list = EmployeeService.find_by_phone_number(phone_number)
            Logger.info(f"Employee FindByPhoneNumber {phone_number}")
            return True, employee_list
        except Exception as e:
            Logger.error(f"Employee FindByPhoneNumber Error: {e}")
            return False, e

    @classmethod
    def find_by_username(cls, username):
        try:
            employee_list = EmployeeService.find_by_username(username)
            Logger.info(f"Employee FindByUsername {username}")
            return True, employee_list
        except Exception as e:
            Logger.error(f"Employee FindByUsername Error: {e}")
            return False, e

    @classmethod
    def find_by_username_and_password(cls, username, password):
        try:
            employee = EmployeeService.find_by_username_and_password(username, password)
            if employee:
                Logger.info(f"Employee FindByUsernameAndPassword {username}")
                return True, employee
            else:
                raise Exception("User Not Found !!!")
        except Exception as e:
            Logger.error(f"Employee FindByUsernameAndPassword Error: {e}")
            return False, e

    @classmethod
    def find_by_role(cls, role):
        try:
            employee_list = EmployeeService.find_by_role(role)
            Logger.info(f"Employee FindByRole {role}")
            return True, employee_list
        except Exception as e:
            Logger.error(f"Employee FindByRole Error: {e}")
            return False, e
