from repository import EmployeeRepository


class EmployeeService:
    employee_repository = EmployeeRepository()

    @classmethod
    def save(cls, employee):
        return cls.employee_repository.save(employee)

    @classmethod
    def update(cls, employee):
        employee_result = cls.employee_repository.find_by_id(employee.employee_id)
        if employee_result:
            return cls.employee_repository.update(employee)
        else:
            raise Exception("Employee Not Found !!!")

    @classmethod
    def delete(cls, employee_id):
        employee = cls.employee_repository.find_by_id(employee_id)
        if employee:
            cls.employee_repository.delete(employee_id)
            return employee
        else:
            raise Exception("Employee Not Found !!!")

    @classmethod
    def find_all(cls):
        return cls.employee_repository.find_all()

    @classmethod
    def find_by_id(cls, employee_id):
        employee = cls.employee_repository.find_by_id(employee_id)
        if employee:
            return employee
        else:
            raise Exception("Employee Not Found !!!")

    @classmethod
    def find_by_firstname_and_lastname(cls, firstname, lastname):
        return cls.employee_repository.find_by_firstname_and_lastname(firstname, lastname)

    @classmethod
    def find_by_phone_number(cls, phone_number):
        return cls.employee_repository.find_by_phone_number(phone_number)

    @classmethod
    def find_by_username(cls, username):
        return cls.employee_repository.find_by_username(username)

    @classmethod
    def find_by_username_and_password(cls, username, password):
        return cls.employee_repository.find_by_username_and_password(username, password)

    @classmethod
    def find_by_role(cls, role):
        return cls.employee_repository.find_by_role(role)
