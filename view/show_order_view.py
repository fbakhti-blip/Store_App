from view import *


class ShowOderView:
    def __init__(self):

        self.window = Tk()
        self.window.title("show_order")
        self.window.geometry("700x280")

        self.order_item = LabelWithEntry(self.window, "OrderItem", 20, 20)
        self.Customer = LabelWithEntry(self.window, "Customer", 20, 60)
        self.DateTime = LabelWithEntry(self.window, "DateTime", 20, 100)
        self.Product = LabelWithEntry(self.window, "Product", 20, 140)
        self.Quantity = LabelWithEntry(self.window, "Quantity", 20, 180)
        self.Price = LabelWithEntry(self.window, "Price", 20, 220)

        self.table = Table(
            self.window,
            ["OrderItem"],
            [375],
            280, 20
        )

        self.window.mainloop()

    def select_from_table(self, selected_order):
        pass
