from view import *

from model import FinancialTransaction, Session
from controller import FinancialTransactionController


class FinancialTransactionView:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1150x440")
        self.window.title("Financial Transaction")

        self.financial_transaction_id = LabelWithEntry(self.window, "Id", 20, 20, state="readonly")
        self.transaction_type = LabelWithEntry(self.window, "Type", 20, 60)
        self.customer_id = LabelWithEntry(self.window, "Customer", 20, 100)
        self.employee_id = LabelWithEntry(self.window, "Employee", 20, 140)
        self.amount = LabelWithEntry(self.window, "Amount", 20, 180)
        self.date_time = LabelWithEntry(self.window, "Date&Time", 20, 220)
        self.payment_id = LabelWithEntry(self.window, "PaymentId", 20, 260)
        self.description = LabelWithEntry(self.window, "Description", 20, 300)

        self.table = Table(
            self.window,
            ["Id", "Type", "Customer", "Employee", "Amount", "Date&Time", "PaymentId", "Description"],
            [60, 60, 140, 140, 100,90,70,180],
            270, 20,
            18,
            self.select_from_table
        )

        Button(self.window, text="Select Transaction", width=19, command=self.select_transaction).place(x=20, y=340)
        Button(self.window, text="Refresh", width=7, command=self.refresh).place(x=180, y=340)
        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=380)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=380)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=380)

        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = FinancialTransactionController.save(self.transaction_type.get(),
                                                                     self.customer_id.get(), self.employee_id.get(),
                                                                     self.amount.get(), self.date_time.get(),
                                                                     self.payment_id.get(), self.description.get())
        if status:
            messagebox.showinfo("Financial_Transaction Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Financial_Transaction", message)

    def edit_click(self):
        status, message = FinancialTransactionController.update(self.financial_transaction_id.get(), self.transaction_type.get(),
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
        self.transaction_type.clear()
        self.customer_id.clear()
        self.employee_id.clear()
        self.amount.clear()
        self.date_time.clear()
        self.payment_id.clear()
        self.description.clear()
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
            self.date_time.set(financial_transaction.date_time)
            self.payment_id.set(financial_transaction.payment_id)
            self.description.set(financial_transaction.description)

    def select_transaction(self):
        if self.financial_transaction_id.get():
            status, Session.financial_transaction = FinancialTransactionController.find_by_id(self.financial_transaction_id.get())
        else:
            messagebox.showerror("Select", "Select Financial Transaction")

    def refresh(self):
        pass
