from view.customer_view import CustomerView
from view.employee_view import EmployeeView
from view.product_view import ProductView
from view import *
from tkcalendar import *
from model import WarehouseTransaction, Session
from controller import WarehouseTransactionController


class WarehouseTransactionView:
    def __init__(self):

        self.window = Tk()
        self.window.geometry("1040x400")
        self.window.title("Warehouse Transaction")

        self.warehouse_transaction_id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, distance=100,
                                                       state="readonly")
        self.product_id = LabelWithEntry(self.window, "Product", 20, 60, distance=100, state="readonly",
                                         on_keypress_function=lambda: ProductView())
        self.quantity = LabelWithEntry(self.window, "Quantity", 20, 100, distance=100)
        self.customer_id = LabelWithEntry(self.window, "Customer", 20, 220, distance=100, state="readonly",
                                          on_keypress_function=lambda: CustomerView())
        self.employee_id = LabelWithEntry(self.window, "Employee", 20, 260, distance=100, state="readonly",
                                          on_keypress_function=lambda: EmployeeView())

        Label(self.window, text="Transaction Date").place(x=20, y=180)
        self.transaction_datetime = DateEntry(self.window, width=17, selectmode="day", date_pattern="y/mm/dd")
        self.transaction_datetime.place(x=120, y=180)

        transaction_type_list = ["input", "output"]
        type_transaction = StringVar(value="input")
        Label(self.window, text="Transaction Type").place(x=20, y=140)
        self.transaction_type = Combobox(
            self.window,
            values=transaction_type_list,
            textvariable=type_transaction,
            width=17,
            state="readonly")
        self.transaction_type.place(x=120, y=140)

        # Search by Customer
        self.search_customer_id = LabelWithEntry(self.window, "Customer", 270, 20, data_type=IntVar, distance=60,
                                                 on_keypress_function=lambda: CustomerView(),
                                                 on_return_function=self.search_by_customer_id)

        # Search by Employee
        self.search_employee_id = LabelWithEntry(self.window, "Employee", 470, 20, data_type=IntVar, distance=60,
                                                 on_keypress_function=lambda: EmployeeView(),
                                                 on_return_function=self.search_by_employee_id)

        # Search by Product
        self.search_product_id = LabelWithEntry(self.window, "Product", 670, 20, data_type=IntVar, distance=50,
                                                on_keypress_function=lambda: ProductView(),
                                                on_return_function=self.search_by_product_id)

        # Search by Transaction Type
        Label(self.window, text="Type").place(x=860, y=20)
        self.search_transaction_type = Combobox(
            self.window,
            values=["", "input", "output"],
            width=16,
            state="readonly")
        self.search_transaction_type.bind("<<ComboboxSelected>>", self.search_by_transaction_type)
        self.search_transaction_type.place(x=895, y=20)

        # Search by Date
        Label(self.window, text="Start Date").place(x=270, y=60)
        self.search_start_date_time = DateEntry(self.window, width=17, selectmode="day", date_pattern="y/mm/dd")
        self.search_start_date_time.bind("<<DateEntrySelected>>", self.search_by_date_time_range)
        self.search_start_date_time.place(x=330, y=60)

        Label(self.window, text="End Date").place(x=470, y=60)
        self.search_end_date_time = DateEntry(self.window, width=17, selectmode="day", date_pattern="y/mm/dd")
        self.search_end_date_time.bind("<<DateEntrySelected>>", self.search_by_date_time_range)
        self.search_end_date_time.place(x=530, y=60)

        self.table = Table(
            self.window,
            ["Id", "Product", "Quantity", "transaction_type", "transaction_datetime", "Customer", "Employee"],
            [40, 130, 60, 100, 120, 150, 140],
            270, 100,
            12,
            self.select_from_table
        )

        Button(self.window, text="Select Transaction", width=19, command=self.select_transaction).place(x=20, y=300)
        Button(self.window, text="Refresh", width=7, command=self.reset_form).place(x=185, y=300)
        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=340)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=340)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=185, y=340)

        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = WarehouseTransactionController.save(Session.product.product_id, self.quantity.get(),
                                                              self.transaction_type.get(),
                                                              self.transaction_datetime.get(),
                                                              Session.customer.customer_id,
                                                              Session.employee.employee_id)
        if status:
            messagebox.showinfo("Warehouse_transaction Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Warehouse_transaction Save Error", message)
        Session.product = None
        Session.customer = None
        Session.employee = None

    def edit_click(self):
        status, message = WarehouseTransactionController.update(self.warehouse_transaction_id.get(),
                                                                self.product_id.get(),
                                                                self.quantity.get(), self.transaction_type.get(),
                                                                self.transaction_datetime.get(),
                                                                self.customer_id.get(), self.employee_id.get())
        if status:
            messagebox.showinfo("Warehouse_transaction Update", message)
            self.reset_form()
        else:
            messagebox.showerror("Warehouse_transaction Update Error", message)

    def delete_click(self):
        status, message = WarehouseTransactionController.delete(self.warehouse_transaction_id.get())
        if status:
            messagebox.showinfo("Warehouse_transaction Delete", message)
            self.reset_form()
        else:
            messagebox.showerror("Warehouse_transaction Delete Error", message)

    def reset_form(self):
        self.warehouse_transaction_id.clear()
        self.product_id.clear()
        self.quantity.clear()
        self.transaction_type.set("input")
        self.transaction_datetime.set_date(None)
        self.customer_id.clear()
        self.employee_id.clear()
        self.search_customer_id.clear()
        self.search_employee_id.clear()
        self.search_product_id.clear()
        self.search_transaction_type.set("")
        self.search_start_date_time.set_date(None)
        self.search_end_date_time.set_date(None)
        status, warehouse_transaction_list = WarehouseTransactionController.find_all()
        self.table.refresh_table(warehouse_transaction_list)

    def select_from_table(self, selected_warehouse_transaction):
        if selected_warehouse_transaction:
            status, warehouse_transaction = WarehouseTransactionController.find_by_id(
                selected_warehouse_transaction[0])
            if status:
                warehouse_transaction = WarehouseTransaction(*selected_warehouse_transaction)
                self.warehouse_transaction_id.set(warehouse_transaction.warehouse_transaction_id)
                self.product_id.set(warehouse_transaction.product_id)
                self.quantity.set(warehouse_transaction.quantity)
                self.transaction_type.set(warehouse_transaction.transaction_type)
                self.transaction_datetime.set_date(warehouse_transaction.transaction_datetime)
                self.customer_id.set(warehouse_transaction.customer_id)
                self.employee_id.set(warehouse_transaction.employee_id)

    def search_by_transaction_type(self, event):
        status, warehouse_transaction_list = WarehouseTransactionController.find_by_transaction_type(
            self.search_transaction_type.get())
        if status and warehouse_transaction_list:
            self.table.refresh_table(warehouse_transaction_list)
        else:
            self.reset_form()

    def search_by_customer_id(self):
        status, warehouse_transaction_list = WarehouseTransactionController.find_by_customer_id(
            Session.customer.customer_id)
        if status and warehouse_transaction_list:
            self.table.refresh_table(warehouse_transaction_list)
            self.search_customer_id.set(Session.customer.full_name())
        else:
            messagebox.showerror("Error", "Customer Not Found")
        Session.customer = None

    def search_by_employee_id(self):
        status, warehouse_transaction_list = WarehouseTransactionController.find_by_employee_id(
            Session.employee.employee_id)
        if status and warehouse_transaction_list:
            self.table.refresh_table(warehouse_transaction_list)
            self.search_employee_id.set(Session.employee.full_name())
        else:
            messagebox.showerror("Error", "Employee Not Found")
        Session.employee = None

    def search_by_product_id(self):
        status, warehouse_transaction_list = WarehouseTransactionController.find_by_product_id(
            Session.product.product_id)
        if status and warehouse_transaction_list:
            self.table.refresh_table(warehouse_transaction_list)
            self.search_product_id.set(Session.product.info())
        else:
            messagebox.showerror("Error", "Product Not Found")
        Session.product = None

    def search_by_date_time_range(self, event):
        status, warehouse_transaction_list = WarehouseTransactionController.find_by_date_time_range(
            self.search_start_date_time.get(),
            self.search_end_date_time.get())
        if status and warehouse_transaction_list:
            self.table.refresh_table(warehouse_transaction_list)
        else:
            self.reset_form()

    def search_by_date_time_range_and_customer_id(self):
        status, warehouse_transaction_list = WarehouseTransactionController.find_by_date_time_range_and_customer_id(
            self.search_start_date_time.get(),
            self.search_end_date_time.get(), Session.customer.customer_id)
        if status and warehouse_transaction_list:
            self.table.refresh_table(warehouse_transaction_list)
            self.search_customer_id.set(Session.customer.full_name())
        else:
            self.reset_form()
        Session.customer = None

    def search_by_date_time_range_and_employee_id(self):
        status, warehouse_transaction_list = WarehouseTransactionController.find_by_date_time_range_and_employee_id(
            self.search_start_date_time.get(),
            self.search_end_date_time.get(), Session.employee.employee_id)
        if status and warehouse_transaction_list:
            self.table.refresh_table(warehouse_transaction_list)
            self.search_employee_id.set(Session.employee.full_name())
        else:
            self.reset_form()
        Session.employee = None

    def select_transaction(self):
        if self.warehouse_transaction_id.get():
            status, Session.warehouse_transaction = WarehouseTransactionController.find_by_id(
                self.warehouse_transaction_id.get())
        else:
            messagebox.showerror("Select", "Select Warehouse Transaction")

    def refresh(self):
        pass
