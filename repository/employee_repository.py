import sqlite3
from model import Employee


class EmployeeRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, employee):
        self.connect()
        self.cursor.execute(
            "insert into employees (first_name, last_name, salary, occupation, phone_number, username, password, role) values (?,?,?,?,?,?,?,?)",
            [employee.first_name, employee.last_name, employee.salary, employee.occupation, employee.phone_number,
             employee.username, employee.password, employee.role])
        employee.employee_id = self.cursor.lastrowid
        self.connection.commit()
        return employee

    def update(self, employee):
        self.connect()
        self.cursor.execute(
            "update employees set first_name=?, last_name=?, salary=?, occupation=?, phone_number=?, username=?, password=?, role=? where id=?",
            [employee.first_name, employee.last_name, employee.salary, employee.occupation, employee.phone_number,
             employee.username, employee.password, employee.role, employee.employee_id])
        self.connection.commit()
        self.disconnect()
        return employee

    def delete(self, id):
        self.connect()
        self.cursor.execute("delete from employees where id=?",
                            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from employees")
        customer_list = [Employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return customer_list

    def find_by_id(self, employee_id):
        self.connect()
        self.cursor.execute("select * from employees where id=?", [employee_id])
        employee = self.cursor.fetchone()
        self.disconnect()
        if employee:
            return Employee(*employee)
        return None

    def find_by_firstname_and_lastname(self, firstname, lastname):
        self.connect()
        self.cursor.execute("select * from employees where first_name like ? and last_name like ? ",
                            [firstname + "%", lastname + "%"])
        employee_list = [Employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return employee_list

    def find_by_phone_number(self, phone_number):
        self.connect()
        self.cursor.execute("select * from employees where phone_number like ?", [phone_number + "%"])
        employee_list = [Employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return employee_list

    def find_by_username(self, username):
        self.connect()
        self.cursor.execute("select * from employees where username=?", [username])
        employee_list = [Employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return employee_list

    def find_by_username_and_password(self, username, password):
        self.connect()
        self.cursor.execute("select * from employees where username=? and password=?", [username, password])
        employee = self.cursor.fetchone()
        self.disconnect()
        return Employee(*employee) if employee else None

    def find_by_role(self, role):
        self.connect()
        self.cursor.execute("select * from employees where role=?", [role])
        employee_list = [Employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return employee_list
