from view import *
from model import WarehouseTransaction, Session
from controller import WarehouseTransactionController


class WarehouseTransactionView:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("970x400")
        self.window.title("Warehouse Transaction")

        self.warehouse_transaction_id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly", distance=100)
        self.product_id = LabelWithEntry(self.window, "Product Id", 20, 60, distance=100)
        self.quantity = LabelWithEntry(self.window, "Quantity", 20, 100, distance=100)
        self.transaction_datetime = LabelWithEntry(self.window, "Transaction Date", 20, 180, distance=100)
        self.customer_id = LabelWithEntry(self.window, "Customer Id", 20, 220, distance=100)
        self.employee_id = LabelWithEntry(self.window, "Employee Id", 20, 260, distance=100)

        transaction_type_list = ["Get", "Receive"]
        type_transaction = StringVar(value="Get")
        Label(self.window, text="Transaction Type").place(x=20, y=140)
        self.transaction_type = Combobox(
            self.window,
            values=transaction_type_list,
            textvariable=type_transaction,
            width=17,
            state="readonly")
        self.transaction_type.place(x=120, y=140)

        self.table = Table(
            self.window,
            ["Id", "Product_Id", "Quantity", "transaction_type", "transaction_datetime", "customer_id", "employee_id"],
            [40, 100, 60, 100, 120, 120, 120],
            275, 20,
            16,
            self.select_from_table
        )

        Button(self.window, text="Select Transaction", width=19, command=self.select_transaction).place(x=20, y=300)
        Button(self.window, text="Refresh", width=7, command=self.refresh).place(x=185, y=300)
        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=340)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=340)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=185, y=340)

        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = WarehouseTransactionController.save(self.product_id.get(), self.quantity.get(),
                                                                     self.transaction_type.get(),
                                                                     self.transaction_datetime.get(),
                                                                     self.customer_id.get(), self.employee_id.get())
        if status:
            messagebox.showinfo("Warehouse_transaction Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Warehouse_transaction Save Error", message)

    def edit_click(self):
        status, message = WarehouseTransactionController.update(self.warehouse_transaction_id.get(), self.product_id.get(),
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
        self.transaction_type.set("get")
        self.transaction_datetime.clear()
        self.customer_id.clear()
        self.employee_id.clear()
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
                self.transaction_datetime.set(warehouse_transaction.transaction_datetime)
                self.customer_id.set(warehouse_transaction.customer_id)
                self.employee_id.set(warehouse_transaction.employee_id)

    def select_transaction(self):
        if self.warehouse_transaction_id.get():
            status, Session.warehouse_transaction = WarehouseTransactionController.find_by_id(self.warehouse_transaction_id.get())
        else:
            messagebox.showerror("Select", "Select Warehouse Transaction")

    def refresh(self):
        pass
