from view import *
from model import Warehouse
from controller import WarehouseController


class WarehouseView:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("600x310")
        self.window.title("warehouse view")

        self.warehouse_id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.product_id = LabelWithEntry(self.window, "Product_Id", 20, 60, data_type=IntVar)
        self.quantity = LabelWithEntry(self.window, "Quantity", 20, 100, data_type=IntVar)

        self.table = Table(
            self.window,
            ["Id", "Product", "Quantity"],
            [40, 150, 100],
            275, 20,
            12,
            self.select_from_table
        )

        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=260)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=260)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=260)
        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = WarehouseController.save(self.product_id.get(), self.quantity.get())
        if status:
            messagebox.showinfo("Warehouse Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Warehouse Save Error", message)

    def edit_click(self):
        status, message = WarehouseController.update(self.warehouse_id.get(), self.product_id.get(),
                                                     self.quantity.get())
        if status:
            messagebox.showinfo("Warehouse Update", message)
            self.reset_form()
        else:
            messagebox.showerror("Warehouse Update Error", message)

    def delete_click(self):
        status, message = WarehouseController.delete(self.warehouse_id.get())
        if status:
            messagebox.showinfo("Warehouse Delete", message)
            self.reset_form()
        else:
            messagebox.showerror("Warehouse Delete Error", message)

    def reset_form(self):
        self.warehouse_id.clear()
        self.product_id.clear()
        self.quantity.clear()
        status, warehouse_list = WarehouseController.find_all()
        self.table.refresh_table(warehouse_list)

    def select_from_table(self, selected_warehouse):
        if selected_warehouse:
            status, warehouse = WarehouseController.find_by_id(selected_warehouse[0])
            if status:
                warehouse = Warehouse(*selected_warehouse)
                self.warehouse_id.set(warehouse.warehouse_id)
                self.product_id.set(warehouse.product_id)
                self.quantity.set(warehouse.quantity)
