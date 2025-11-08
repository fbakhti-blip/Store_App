from view import *


class ShowOrderView:
    def __init__(self):
        self.window = Tk()
        self.window.title("show_order")
        self.window.geometry("920x270")

        self.order_item = LabelWithEntry(self.window, "OrderItem", 20, 20)
        self.customer_id = LabelWithEntry(self.window, "Customer", 20, 60, data_type=IntVar)
        self.date_time = LabelWithEntry(self.window, "DateTime", 20, 100)
        self.product_id = LabelWithEntry(self.window, "Product", 20, 140, data_type=IntVar)
        self.quantity = LabelWithEntry(self.window, "Quantity", 20, 180, data_type=IntVar)
        self.price = LabelWithEntry(self.window, "Price", 20, 220, data_type=IntVar)

        self.table = Table(
            self.window,
            ["OrderItem", "Order", "Product", "Quantity", "Price", "Discount", "Description"],
            [80, 60, 120, 70, 80, 80, 120],
            280, 20,
            10,
            self.select_from_table
        )

        self.window.mainloop()

    def select_from_table(self, selected_order_item):
        pass
