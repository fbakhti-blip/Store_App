from view import *
from model import Employee, Session
from controller import EmployeeController


class EmployeeView:
    def __init__(self):

        self.window = Tk()
        self.window.title("Employee")
        self.window.geometry("1090x470")

        self.employee_id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.first_name = LabelWithEntry(self.window, "FirstName", 20, 60)
        self.last_name = LabelWithEntry(self.window, "LastName", 20, 100)
        self.salary = LabelWithEntry(self.window, "Salary", 20, 140, data_type=IntVar)
        self.phone_number = LabelWithEntry(self.window, "PhoneNumber", 20, 220)
        self.username = LabelWithEntry(self.window, "Username", 20, 260)
        self.password = LabelWithEntry(self.window, "Password", 20, 300)

        occupation_list = ["cashier", "manager", "sale", "storekeeper"]
        type_occupation = StringVar(value="cashier")
        Label(self.window, text="Occupation").place(x=20, y=180)
        self.occupation = Combobox(
            self.window,
            values=occupation_list,
            textvariable=type_occupation,
            width=17,
            state="readonly")
        self.occupation.place(x=110, y=180)

        role_list = ["cashier", "manager", "sale", "storekeeper"]
        type_role = StringVar(value="cashier")
        Label(self.window, text="Role").place(x=20, y=340)
        self.role = Combobox(
            self.window,
            values=role_list,
            textvariable=type_role,
            width=17,
            state="readonly")
        self.role.place(x=110, y=340)

        self.search_username = LabelWithEntry(self.window, "Username", 270, 20, distance=60,
                                              on_keypress_function=self.search_by_username)

        self.search_password = LabelWithEntry(self.window, "Password", 470, 20, distance=60,
                                              on_keypress_function=self.search_by_password)

        Label(self.window, text="Role").place(x=670, y=20)
        self.search_role = Combobox(
            self.window,
            values=["", "cashier", "manager", "sale", "storekeeper"],
            width=14,
            state="readonly")
        self.search_role.bind("<<ComboboxSelected>>", self.search_by_role)
        self.search_role.place(x=700, y=20)

        self.table = Table(self.window,
                           ["Id", "FirstName", "LastName", "Salary", "Occupation", "PhoneNumber", "Username",
                            "Password", "Role"],
                           [40, 100, 100, 70, 90, 100, 100, 100, 90],
                           270, 60,
                           18,
                           self.select_from_table
                           )

        Button(self.window, text="Select Employee", width=19, command=self.select_employee).place(x=20, y=380)
        Button(self.window, text="Refresh", width=7, command=self.reset_form).place(x=180, y=380)
        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=420)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=420)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=420)

        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = EmployeeController.save(self.first_name.get(), self.last_name.get(), self.salary.get(),
                                                  self.occupation.get(),
                                                  self.phone_number.get(), self.username.get(), self.password.get(),
                                                  self.role.get())
        if status:
            messagebox.showinfo("Employee Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Employee Save Error", message)

    def edit_click(self):
        status, message = EmployeeController.update(self.employee_id.get(), self.first_name.get(), self.last_name.get(),
                                                    self.salary.get(),
                                                    self.occupation.get(), self.phone_number.get(), self.username.get(),
                                                    self.password.get(), self.role.get())
        if status:
            messagebox.showinfo("Employee update", message)
            self.reset_form()
        else:
            messagebox.showerror("Employee update Error", message)

    def delete_click(self):
        status, message = EmployeeController.delete(self.employee_id.get())
        if status:
            messagebox.showinfo("Employee Delete", message)
            self.reset_form()
        else:
            messagebox.showerror("Employee Delete Error", message)

    def reset_form(self):
        self.employee_id.clear()
        self.first_name.clear()
        self.last_name.clear()
        self.salary.clear()
        self.occupation.set("cashier")
        self.phone_number.clear()
        self.username.clear()
        self.password.clear()
        self.role.set("cashier")
        self.search_username.clear()
        self.search_password.clear()
        self.search_role.set("")
        status, employee_list = EmployeeController.find_all()
        self.table.refresh_table(employee_list)

    def select_from_table(self, selected_employee):
        if selected_employee:
            status, employee = EmployeeController.find_by_id(selected_employee[0])
            if status:
                employee = Employee(*selected_employee)
                self.employee_id.set(employee.employee_id)
                self.first_name.set(employee.first_name)
                self.last_name.set(employee.last_name)
                self.salary.set(employee.salary)
                self.occupation.set(employee.occupation)
                self.phone_number.set(employee.phone_number)
                self.username.set(employee.username)
                self.password.set(employee.password)
                self.role.set(employee.role)

    def search_by_username(self):
        status, employee_list = EmployeeController.find_by_username(self.search_username.get())
        if status and employee_list:
            self.table.refresh_table(employee_list)

    def search_by_password(self):
        status, employee_list = EmployeeController.find_by_username_and_password(self.search_username.get(),
                                                                                 self.search_password.get())
        if status and employee_list:
            self.table.refresh_table(employee_list)

    def search_by_role(self, event):
        status, employee_list = EmployeeController.find_by_role(self.search_role.get())
        if status and employee_list:
            self.table.refresh_table(employee_list)
        else:
            self.reset_form()

    def select_employee(self):
        if self.employee_id.get():
            status, Session.employee = EmployeeController.find_by_id(self.employee_id.get())
        else:
            messagebox.showerror("Select", "Select Employee")

    def refresh(self):
        pass
