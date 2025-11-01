from tkinter import *
from PIL import ImageTk, Image
from model import Session
from view.customer_view import CustomerView
from view.employee_view import EmployeeView
from view.bank_view import BankView
from view.product_view import ProductView
from view.warehouse_view import WarehouseView
from view.order_view import OrderView
from view.order_item_view import OrderItemView
from view.payment_view import PaymentView
from view.warehouse_transaction_view import WarehouseTransactionView
from view.financial_transaction_view import FinancialTransactionView
from view.delivery_view import DeliveryView


class DashboardView:
    def employee_view(self):
        ui = EmployeeView()

    def customer_view(self):
        ui = CustomerView()

    def bank_view(self):
        ui = BankView()

    def product_view(self):
        ui = ProductView()

    def warehouse_view(self):
        ui = WarehouseView()

    def order_view(self):
        ui = OrderView()

    def order_item_view(self):
        ui = OrderItemView()

    def payment_view(self):
        ui = PaymentView()

    def warehouse_transaction_view(self):
        ui = WarehouseTransactionView()

    def financial_transaction_view(self):
        ui = FinancialTransactionView()

    def delivery_view(self):
        ui = DeliveryView()

    def __init__(self):

        self.employee = Session.employee

        font = ("Arial", 18, "bold")
        width = 24
        background_color = "violet red"
        foreground_color = "white"
        y_dist = 60

        self.window = Tk()
        self.window.geometry("540x900")
        self.window.title("Dashboard")
        self.window.config(bg="white")

        image = Image.open("./view/images/img.png")
        image = ImageTk.PhotoImage(image)

        Label(self.window, image=image).place(x=195, y=15)

        Button(self.window, font=font, width=width, bg=background_color, fg=foreground_color, text="Employee",
               command=self.employee_view).place(x=80, y=180)
        Button(self.window, font=font, width=width, bg=background_color, fg=foreground_color, text="Customer",
               command=self.customer_view).place(x=80, y=180 + y_dist * 1)
        Button(self.window, font=font, width=width, bg=background_color, fg=foreground_color, text="Bank",
               command=self.bank_view).place(x=80, y=180 + y_dist * 2)
        Button(self.window, font=font, width=width, bg=background_color, fg=foreground_color, text="Product",
               command=self.product_view).place(x=80, y=180 + y_dist * 3)
        Button(self.window, font=font, width=width, bg=background_color, fg=foreground_color, text="Warehouse",
               command=self.warehouse_view).place(x=80, y=180 + y_dist * 4)
        Button(self.window, font=font, width=width, bg=background_color, fg=foreground_color, text="Order",
               command=self.order_view).place(x=80, y=180 + y_dist * 5)
        Button(self.window, font=font, width=width, bg=background_color, fg=foreground_color, text="OrderItem",
               command=self.order_item_view).place(x=80, y=180 + y_dist * 6)
        Button(self.window, font=font, width=width, bg=background_color, fg=foreground_color, text="Payment",
               command=self.payment_view).place(x=80, y=180 + y_dist * 7)
        Button(self.window, font=font, width=width, bg=background_color, fg=foreground_color,
               text="Financial Transaction",
               command=self.financial_transaction_view).place(x=80, y=180 + y_dist * 8)
        Button(self.window, font=font, width=width, bg=background_color, fg=foreground_color,
               text="Warehouse Transaction",
               command=self.warehouse_transaction_view).place(x=80, y=180 + y_dist * 9)
        Button(self.window, font=font, width=width, bg=background_color, fg=foreground_color, text="Delivery",
               command=self.delivery_view).place(x=80, y=180 + y_dist * 10)

        employee_name = self.employee.username if self.employee else "Not Logged In"
        Label(self.window, text=f"Employee : {employee_name}", font=font, bg="white").place(x=80, y=850)

        self.window.mainloop()
