from view.customer_view import CustomerView
from view.employee_view import EmployeeView
from view.payment_view import PaymentView
from view import *
from tkcalendar import *

from model import FinancialTransaction, Session
from controller import FinancialTransactionController


class FinancialTransactionView:
    def __init__(self):

        self.window = Tk()
        self.window.geometry("1150x440")
        self.window.title("Financial Transaction")

        self.financial_transaction_id = LabelWithEntry(self.window, "Id", 20, 20, state="readonly")
        self.customer_id = LabelWithEntry(self.window, "Customer", 20, 100, state="readonly",
                                          on_keypress_function=lambda: CustomerView())
        self.employee_id = LabelWithEntry(self.window, "Employee", 20, 140, state="readonly",
                                          on_keypress_function=lambda: EmployeeView())
        self.amount = LabelWithEntry(self.window, "Amount", 20, 180)
        self.payment_id = LabelWithEntry(self.window, "PaymentId", 20, 260, state="readonly",
                                         on_keypress_function=lambda: PaymentView())
        self.description = LabelWithEntry(self.window, "Description", 20, 300)

        Label(self.window, text="Date&Time").place(x=20, y=220)
        self.date_time = DateEntry(self.window, width=17, selectmode="day", date_pattern="y/mm/dd")
        self.date_time.place(x=110, y=220)

        transaction_type_list = ["sale", "purchase", "salary", "expense"]
        type_transaction = StringVar(value="sale")
        Label(self.window, text="Type").place(x=20, y=60)
        self.transaction_type = Combobox(
            self.window,
            values=transaction_type_list,
            textvariable=type_transaction,
            width=17,
            state="readonly")
        self.transaction_type.place(x=110, y=60)

        # Search by Customer
        self.search_customer_id = LabelWithEntry(self.window, "Customer", 270, 20, data_type=IntVar, distance=60,
                                                 on_keypress_function=lambda: CustomerView(),
                                                 on_return_function=self.search_by_customer_id)

        # Search by Employee
        self.search_employee_id = LabelWithEntry(self.window, "Employee", 470, 20, data_type=IntVar, distance=60,
                                                 on_keypress_function=lambda: EmployeeView(),
                                                 on_return_function=self.search_by_employee_id)

        # Search by Payment
        self.search_payment_id = LabelWithEntry(self.window, "Payment", 670, 20, data_type=IntVar, distance=60,
                                                on_keypress_function=lambda: PaymentView(),
                                                on_return_function=self.search_by_payment_id)

        # Search by Transaction Type
        Label(self.window, text="Type").place(x=870, y=20)
        self.search_transaction_type = Combobox(
            self.window,
            values=["", "sale", "purchase", "salary", "expense"],
            width=15,
            state="readonly")
        self.search_transaction_type.bind("<<ComboboxSelected>>", self.search_by_transaction_type)
        self.search_transaction_type.place(x=910, y=20)

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
            ["Id", "Type", "Customer", "Employee", "Amount", "Date&Time", "PaymentId", "Description"],
            [60, 60, 140, 140, 100, 90, 70, 180],
            270, 100,
            14,
            self.select_from_table
        )

        Button(self.window, text="Select Transaction", width=19, command=self.select_transaction).place(x=20, y=340)
        Button(self.window, text="Refresh", width=7, command=self.reset_form).place(x=180, y=340)
        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=380)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=380)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=380)

        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = FinancialTransactionController.save(self.transaction_type.get(),
                                                              Session.customer.customer_id,
                                                              Session.employee.employee_id,
                                                              self.amount.get(), self.date_time.get(),
                                                              Session.payment.payment_id, self.description.get())
        if status:
            messagebox.showinfo("Financial_Transaction Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Financial_Transaction", message)
        Session.customer = None
        Session.employee = None
        Session.payment = None

    def edit_click(self):
        status, message = FinancialTransactionController.update(self.financial_transaction_id.get(),
                                                                self.transaction_type.get(),
                                                                self.customer_id.get(), self.employee_id.get(),
                                                                self.amount.get(), self.date_time.get(),
                                                                self.payment_id.get(), self.description.get())
        if status:
            messagebox.showinfo("Financial_Transaction update", message)
            self.reset_form()
        else:
            messagebox.showerror("Financial_Transaction update error", message)

    def delete_click(self):
        status, message = FinancialTransactionController.delete(self.financial_transaction_id.get())
        if status:
            messagebox.showinfo("Financial_Transaction update", message)
            self.reset_form()
        else:
            messagebox.showerror("Financial_Transaction update error", message)

    def reset_form(self):
        self.financial_transaction_id.clear()
        self.transaction_type.set("sale")
        self.customer_id.clear()
        self.employee_id.clear()
        self.amount.clear()
        self.date_time.set_date(None)
        self.payment_id.clear()
        self.payment_id.clear()
        self.description.clear()
        self.search_customer_id.clear()
        self.search_employee_id.clear()
        self.search_payment_id.clear()
        self.search_transaction_type.set("")
        self.search_start_date_time.set_date(None)
        self.search_end_date_time.set_date(None)
        status, financial_transaction_list = FinancialTransactionController.find_all()
        self.table.refresh_table(financial_transaction_list)

    def select_from_table(self, selected_financial_transaction):
        if selected_financial_transaction:
            financial_transaction = FinancialTransaction(*selected_financial_transaction)
            self.financial_transaction_id.set(financial_transaction.financial_transaction_id)
            self.transaction_type.set(financial_transaction.transaction_type)
            self.customer_id.set(financial_transaction.customer_id)
            self.employee_id.set(financial_transaction.employee_id)
            self.amount.set(financial_transaction.amount)
            self.date_time.set_date(financial_transaction.date_time)
            self.payment_id.set(financial_transaction.payment_id)
            self.description.set(financial_transaction.description)

    def search_by_transaction_type(self, event):
        status, financial_transaction_list = FinancialTransactionController.find_by_transaction_type(
            self.search_transaction_type.get())
        if status and financial_transaction_list:
            self.table.refresh_table(financial_transaction_list)
        else:
            self.reset_form()

    def search_by_customer_id(self):
        status, financial_transaction_list = FinancialTransactionController.find_by_customer_id(
            Session.customer.customer_id)
        if status and financial_transaction_list:
            self.table.refresh_table(financial_transaction_list)
            self.search_customer_id.set(Session.customer.full_name())
        else:
            messagebox.showerror("Error", "Customer Not Found")
        Session.customer = None

    def search_by_employee_id(self):
        status, financial_transaction_list = FinancialTransactionController.find_by_employee_id(
            Session.employee.employee_id)
        if status and financial_transaction_list:
            self.table.refresh_table(financial_transaction_list)
            self.search_employee_id.set(Session.employee.full_name())
        else:
            messagebox.showerror("Error", "Employee Not Found")
        Session.employee = None

    def search_by_payment_id(self):
        status, financial_transaction_list = FinancialTransactionController.find_by_payment_id(
            Session.payment.payment_id)
        if status and financial_transaction_list:
            self.table.refresh_table(financial_transaction_list)
            self.search_payment_id.set(Session.payment.payment_id)
        else:
            messagebox.showerror("Error", "Payment Not Found")
        Session.payment = None

    def search_by_date_time_range(self, event):
        status, financial_transaction_list = FinancialTransactionController.find_by_date_time_range(
            self.search_start_date_time.get(),
            self.search_end_date_time.get())
        if status and financial_transaction_list:
            self.table.refresh_table(financial_transaction_list)
        else:
            self.reset_form()

    def search_by_date_time_range_and_customer_id(self):
        status, financial_transaction_list = FinancialTransactionController.find_by_date_time_range_and_customer_id(
            self.search_start_date_time.get(),
            self.search_end_date_time.get(), Session.customer.customer_id)
        if status and financial_transaction_list:
            self.table.refresh_table(financial_transaction_list)
            self.search_customer_id.set(Session.customer.full_name())
        else:
            self.reset_form()
        Session.customer = None

    def search_by_date_time_range_and_employee_id(self):
        status, financial_transaction_list = FinancialTransactionController.find_by_date_time_range_and_employee_id(
            self.search_start_date_time.get(),
            self.search_end_date_time.get(), Session.employee.employee_id)
        if status and financial_transaction_list:
            self.table.refresh_table(financial_transaction_list)
            self.search_employee_id.set(Session.employee.full_name())
        else:
            self.reset_form()
        Session.employee = None

    def select_transaction(self):
        if self.financial_transaction_id.get():
            status, Session.financial_transaction = FinancialTransactionController.find_by_id(
                self.financial_transaction_id.get())
        else:
            messagebox.showerror("Select", "Select Financial Transaction")

    def refresh(self):
        pass
