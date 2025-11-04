from view import *
from model import Bank, Session
from controller import BankController


class BankView:
    def __init__(self):

        self.window = Tk()
        self.window.geometry("750x320")
        self.window.title("Bank")

        self.bank_id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.bank_name = LabelWithEntry(self.window, "BankName", 20, 60)
        self.balance = LabelWithEntry(self.window, "Balance", 20, 140, data_type=IntVar)
        self.description = LabelWithEntry(self.window, "Description", 20, 180)

        account_name_list = ["checking", "saving", "current"]
        name_account = StringVar(value="checking")
        Label(self.window, text="AccountName").place(x=20, y=100)
        self.account_name = Combobox(
            self.window,
            values=account_name_list,
            textvariable=name_account,
            width=17,
            state="readonly")
        self.account_name.place(x=110, y=100)

        self.table = Table(
            self.window,
            ["Id", "BankName", "AccountName", "Balance", "Description"],
            [40, 100, 100, 60, 150],
            270, 20,
            12,
            self.select_from_table
        )

        Button(self.window, text="Select Bank", width=19, command=self.select_bank).place(x=20, y=220)
        Button(self.window, text="Refresh", width=7, command=self.refresh).place(x=180, y=220)
        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=260)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=260)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=260)

        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = BankController.save(self.bank_name.get(), self.account_name.get(), self.balance.get(),
                                              self.description.get())
        if status:
            messagebox.showinfo("Bank Saved", message)
            self.reset_form()
        else:
            messagebox.showerror("Bank Save Error", message)

    def edit_click(self):
        status, message = BankController.update(self.bank_id.get(), self.bank_name.get(), self.account_name.get(),
                                                self.balance.get(), self.description.get())
        if status:
            messagebox.showinfo("Bank Updated", message)
            self.reset_form()
        else:
            messagebox.showerror("Bank Update Error", message)

    def delete_click(self):
        status, message = BankController.delete(self.bank_id.get())
        if status:
            messagebox.showinfo("Bank Deleted", message)
            self.reset_form()
        else:
            messagebox.showerror("Bank Delete Error", message)

    def reset_form(self):
        self.bank_id.clear()
        self.bank_name.clear()
        self.account_name.set("checking")
        self.balance.clear()
        self.description.clear()
        status, bank_list = BankController.find_all()
        self.table.refresh_table(bank_list)

    def select_from_table(self, selected_bank):
        if selected_bank:
            status, bank = BankController.find_by_id(selected_bank[0])
            if status:
                bank = Bank(*selected_bank)
                self.bank_id.set(bank.bank_id)
                self.bank_name.set(bank.name)
                self.account_name.set(bank.account)
                self.balance.set(bank.balance)
                self.description.set(bank.description)

    def select_bank(self):
        if self.bank_id.get():
            status, Session.bank = BankController.find_by_id(self.bank_id.get())
        else:
            messagebox.showerror("Select", "Select Bank")

    def refresh(self):
        self.reset_form()
