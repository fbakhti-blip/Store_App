from view.product_view import ProductView
from view import *
from model import Warehouse, Session
from controller import WarehouseController


class WarehouseView:
    def __init__(self):

        self.window = Tk()
        self.window.geometry("910x320")
        self.window.title("Warehouse View")

        self.warehouse_id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.product_id = LabelWithEntry(self.window, "Product", 20, 60, data_type=IntVar, state="readonly",
                                         on_keypress_function=lambda: ProductView())
        self.quantity = LabelWithEntry(self.window, "Quantity", 20, 100, data_type=IntVar)

        # Search by Product
        self.search_product_id = LabelWithEntry(self.window, "Product Id", 275, 20, data_type=IntVar, distance=65,
                                                on_keypress_function=self.search_by_product_id,
                                                on_keypress_function2=lambda: ProductView())
        # Search by Quantity Less Than
        self.search_quantity_less_than = LabelWithEntry(self.window, "Quantity<?", 480, 20, data_type=IntVar,
                                                        distance=70,
                                                        on_keypress_function=self.search_by_quantity_less_than)
        # Search by Quantity More Than
        self.search_quantity_more_than = LabelWithEntry(self.window, "Quantity>?", 690, 20, data_type=IntVar,
                                                        distance=70,
                                                        on_keypress_function=self.search_by_quantity_more_than)

        self.table = Table(
            self.window,
            ["Id", "Product", "Quantity"],
            [60, 320, 225],
            275, 60,
            10,
            self.select_from_table
        )

        Button(self.window, text="Select Item", width=19, command=self.select_warehouse_item).place(x=20, y=220)
        Button(self.window, text="Refresh", width=7, command=self.reset_form).place(x=180, y=220)
        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=260)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=260)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=260)

        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = WarehouseController.save(Session.product.product_id, self.quantity.get())
        if status:
            messagebox.showinfo("Warehouse Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Warehouse Save Error", message)
        Session.product = None

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

    def search_by_product_id(self):
        self.search_product_id.clear()
        status, warehouse_list = WarehouseController.find_by_product_id(Session.product.product_id)
        if status and warehouse_list:
            self.search_product_id.set(Session.product.name + " " + Session.product.brand)
            self.table.refresh_table(warehouse_list)
        else:
            messagebox.showerror("Search Error", "Item Not Found!")

    def search_by_quantity_less_than(self):
        status, warehouse_list = WarehouseController.find_by_quantity_less_than(self.search_quantity_less_than.get())
        if status and warehouse_list:
            self.table.refresh_table(warehouse_list)
        else:
            messagebox.showerror("Search Error", "Not Found!")

    def search_by_quantity_more_than(self):
        status, warehouse_list = WarehouseController.find_by_quantity_more_than(self.search_quantity_more_than.get())
        if status and warehouse_list:
            self.table.refresh_table(warehouse_list)
        else:
            messagebox.showerror("Search Error", "Not Found!")

    def select_warehouse_item(self):
        if self.warehouse_id.get():
            status, Session.warehouse = WarehouseController.find_by_id(self.warehouse_id.get())
        else:
            messagebox.showerror("Select", "Select Warehouse Item")

    def refresh(self):
        pass
