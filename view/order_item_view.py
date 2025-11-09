from view.order_view import OrderView
from view.product_view import ProductView
from view import *

from model import OrderItem, Session
from controller import OrderItemController


class OrderItemView:
    def __init__(self):

        self.window = Tk()
        self.window.title("Order Item")
        self.window.geometry("950x400")

        self.order_item_id = LabelWithEntry(self.window, "Id", 20, 20, distance=95, data_type=IntVar, state="readonly")
        self.order_id = LabelWithEntry(self.window, "Order Id", 20, 60, distance=95, data_type=IntVar, state="readonly",
                                       on_keypress_function=lambda: OrderView())
        self.product_id = LabelWithEntry(self.window, "Product", 20, 100, distance=95, data_type=IntVar,
                                         state="readonly",
                                         on_keypress_function=lambda: ProductView())
        self.quantity = LabelWithEntry(self.window, "Quantity", 20, 140, distance=95, data_type=IntVar)
        self.price = LabelWithEntry(self.window, "Price", 20, 180, distance=95, data_type=IntVar)
        self.discount = LabelWithEntry(self.window, "Discount", 20, 220, distance=95, data_type=IntVar)
        self.description = LabelWithEntry(self.window, "Description", 20, 260, distance=95)

        self.search_order_id = LabelWithEntry(self.window, "Order Id", 300, 20, data_type=IntVar, distance=60,
                                              on_keypress_function=lambda: OrderView(),
                                              on_return_function=self.search_by_order_id)
        self.search_product_id = LabelWithEntry(self.window, "Product", 500, 20, data_type=IntVar, distance=60,
                                                on_keypress_function=lambda: ProductView(),
                                                on_return_function=self.search_by_product_id)
        self.search_quantity = LabelWithEntry(self.window, "Quantity<?", 710, 20, data_type=IntVar, distance=70,
                                              on_keypress_function=self.search_by_quantity)

        self.table = Table(self.window,
                           ["Id", "Order Id", "Product", "Quantity", "Price", "Discount", "Description"],
                           [40, 60, 140, 60, 100, 60, 145]
                           , 300, 60,
                           14,
                           self.select_from_table
                           )

        Button(self.window, text="Select OrderItem", width=19, command=self.select_order_item).place(x=20, y=300)
        Button(self.window, text="Refresh", width=7, command=self.reset_form).place(x=180, y=300)
        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=340)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=340)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=340)

        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = OrderItemController.save(Session.order.order_id, Session.product.product_id,
                                                   self.quantity.get(),
                                                   self.price.get(), self.discount.get(), self.description.get())
        if status:
            messagebox.showinfo("Order Item Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Order Item Save Error", message)

    def edit_click(self):
        status, message = OrderItemController.update(self.order_item_id.get(), self.order_id.get(),
                                                     self.product_id.get(), self.quantity.get(),
                                                     self.price.get(), self.discount.get(), self.description.get())
        if status:
            messagebox.showinfo("Order Item Update", message)
            self.reset_form()
        else:
            messagebox.showerror("Order Item Update Error", message)

    def delete_click(self):
        status, message = OrderItemController.delete(self.order_item_id.get())
        if status:
            messagebox.showinfo("Order Item Delete", message)
            self.reset_form()
        else:
            messagebox.showerror("Order Item Delete Error", message)

    def reset_form(self):
        self.order_item_id.clear()
        self.order_id.clear()
        self.product_id.clear()
        self.quantity.clear()
        self.price.clear()
        self.discount.clear()
        self.description.clear()
        self.search_order_id.clear()
        self.search_product_id.clear()
        self.search_quantity.clear()
        status, order_item_list = OrderItemController.find_all()
        self.table.refresh_table(order_item_list)

    def select_from_table(self, selected_order_item):
        if selected_order_item:
            status, order_item = OrderItemController.find_by_id(selected_order_item[0])
            if status:
                order_item = OrderItem(*selected_order_item)
                self.order_item_id.set(order_item.order_item_id)
                self.order_id.set(order_item.order_id)
                self.product_id.set(order_item.product_id)
                self.quantity.set(order_item.quantity)
                self.price.set(order_item.price)
                self.discount.set(order_item.discount)
                self.description.set(order_item.description)

    def search_by_order_id(self):
        status, order_item_list = OrderItemController.find_by_order_id(Session.order.order_id)
        if status and order_item_list:
            self.search_order_id.set(Session.order.order_id)
            self.table.refresh_table(order_item_list)
        else:
            messagebox.showerror("Search Error", "Order Not Found!")

    def search_by_product_id(self):
        status, order_item_list = OrderItemController.find_by_product_id(Session.product.product_id)
        if status and order_item_list:
            self.search_product_id.set(Session.product.name + " " + Session.product.brand)
            self.table.refresh_table(order_item_list)
        else:
            messagebox.showerror("Search Error", "Product Not Found!")

    def search_by_quantity(self):
        status, order_item_list = OrderItemController.find_by_quantity_less_than(self.search_quantity.get())
        if status and order_item_list:
            self.table.refresh_table(order_item_list)
        else:
            messagebox.showerror("Search Error", "Item Not Found!")

    def select_order_item(self):
        if self.order_item_id.get():
            status, Session.order_item = OrderItemController.find_by_id(self.order_item_id.get())
        else:
            messagebox.showerror("Select", "Select Order Item")

    def refresh(self):
        pass
