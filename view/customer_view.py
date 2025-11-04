from view import *

from model import Customer, Session
from controller import CustomerController


class CustomerView:
    def __init__(self):

        self.window = Tk()
        self.window.geometry("800x310")
        self.window.title("Customer")

        self.customer_id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.first_name = LabelWithEntry(self.window, "FirstName", 20, 60)
        self.last_name = LabelWithEntry(self.window, "LastName", 20, 100)
        self.phone_number = LabelWithEntry(self.window, "PhoneNumber", 20, 140)
        self.address = LabelWithEntry(self.window, "Address", 20, 180)

        self.table = Table(
            self.window,
            ["Id", "first_name", "last_name", "phone_number", "address"],
            [40, 100, 100, 100, 160],
            275, 20,
            12,
            self.select_from_table
        )

        Button(self.window, text="Select Customer", width=19, command=self.select_customer).place(x=20, y=220)
        Button(self.window, text="Refresh", width=7, command=self.refresh).place(x=180, y=220)
        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=260)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=260)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=260)

        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = CustomerController.save(self.first_name.get(), self.last_name.get(),
                                                  self.phone_number.get(), self.address.get())
        if status:
            messagebox.showinfo("Customer Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Customer Save Error", message)

    def edit_click(self):
        status, message = CustomerController.update(self.customer_id.get(), self.first_name.get(), self.last_name.get(),
                                                    self.phone_number.get(), self.address.get())
        if status:
            messagebox.showinfo("Customer Update", message)
            self.reset_form()
        else:
            messagebox.showerror("Customer Update Error", message)

    def delete_click(self):
        status, message = CustomerController.delete(self.customer_id.get())
        if status:
            messagebox.showinfo("Customer Delete", message)
            self.reset_form()
        else:
            messagebox.showerror("Customer Delete Error", message)

    def reset_form(self):
        self.customer_id.clear()
        self.first_name.clear()
        self.last_name.clear()
        self.phone_number.clear()
        self.address.clear()
        status, customer_list = CustomerController.find_all()
        self.table.refresh_table(customer_list)

    def select_from_table(self, selected_customer):
        if selected_customer:
            status, customer = CustomerController.find_by_id(selected_customer[0])
            if status:
                customer = Customer(*selected_customer)
                self.customer_id.set(customer.customer_id)
                self.first_name.set(customer.first_name)
                self.last_name.set(customer.last_name)
                self.phone_number.set(customer.phone_number)
                self.address.set(customer.address)

    def select_customer(self):
        if self.customer_id.get():
            status, Session.customer = CustomerController.find_by_id(self.customer_id.get())
        else:
            messagebox.showerror("Select", "Select Customer")

    def refresh(self):
        self.reset_form()
