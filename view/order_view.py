from view.customer_view import CustomerView
from view.employee_view import EmployeeView
from view.payment_view import PaymentView
from view.warehouse_transaction_view import WarehouseTransactionView
from view.show_order_view import ShowOrderView
from view import *
from tkcalendar import *

from model import Order, OrderItem, Session
from controller import OrderController
from controller import OrderItemController


class OrderView:
    def __init__(self):

        self.window = Tk()
        self.window.title("Order")
        self.window.geometry("1360x535")

        self.order_id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.customer_id = LabelWithEntry(self.window, "Customer Id", 20, 60, data_type=IntVar, state="readonly",
                                          on_keypress_function=lambda: CustomerView())
        self.employee_id = LabelWithEntry(self.window, "Employee Id", 20, 100, data_type=IntVar, state="readonly",
                                          on_keypress_function=lambda: EmployeeView())
        self.date_time = LabelWithEntry(self.window, "Date & Time", 20, 140)
        self.payment_id = LabelWithEntry(self.window, "Payment Id", 20, 180, data_type=IntVar, state="readonly",
                                         on_keypress_function=lambda: PaymentView())
        self.warehouse_transaction_id = LabelWithEntry(self.window, "Ware Trans Id", 20, 225, data_type=IntVar,
                                                       state="readonly",
                                                       on_keypress_function=lambda: WarehouseTransactionView())
        self.tax = LabelWithEntry(self.window, "Tax", 20, 270, data_type=IntVar)
        self.total_discount = LabelWithEntry(self.window, "Total Discount", 20, 310, data_type=IntVar)
        self.total_amount = LabelWithEntry(self.window, "Total Amount", 20, 350, data_type=IntVar)

        order_type_list = ["Basket", "Sell", "Buy"]
        type_order = StringVar(value="Basket")
        Label(self.window, text="Order Type").place(x=20, y=390)
        self.order_type = Combobox(
            self.window,
            values=order_type_list,
            textvariable=type_order,
            width=17,
            state="readonly")
        self.order_type.place(x=110, y=390)

        # Search by Customer
        self.search_customer_id = LabelWithEntry(self.window, "Customer Id", 280, 20, data_type=IntVar, distance=75,
                                                 on_keypress_function=self.search_by_customer_id)

        # Search by Employee
        self.search_employee_id = LabelWithEntry(self.window, "Employee Id", 500, 20, data_type=IntVar, distance=75,
                                                 on_keypress_function=self.search_by_employee_id)

        # Search by Date
        Label(self.window, text="Start Date").place(x=720, y=20)
        self.search_start_date_time = DateEntry(self.window, width=16, selectmode="day", date_pattern="y/mm/dd")
        self.search_start_date_time.bind("<<DateEntrySelected>>", self.search_by_date_time_range)
        self.search_start_date_time.place(x=780, y=20)

        Label(self.window, text="End Date").place(x=920, y=20)
        self.search_end_date_time = DateEntry(self.window, width=16, selectmode="day", date_pattern="y/mm/dd")
        self.search_end_date_time.bind("<<DateEntrySelected>>", self.search_by_date_time_range)
        self.search_end_date_time.place(x=980, y=20)

        # self.search_start_date_time = LabelWithEntry(self.window, "Start Date", 720, 20, distance=60,
        #                                              on_keypress_function=self.pick_start_date,
        #                                              on_keypress_function2=self.search_by_date_time_range)
        #
        # self.search_end_date_time = LabelWithEntry(self.window, "End Date", 920, 20, distance=55,
        #                                            on_keypress_function=self.pick_end_date,
        #                                            on_keypress_function2=self.search_by_date_time_range)

        # Search by Order Type
        Label(self.window, text="Order Type").place(x=1120, y=20)
        self.search_order_type = Combobox(
            self.window,
            values=["", "Basket", "Sell", "Buy"],
            width=17,
            state="readonly")
        self.search_order_type.bind("<<ComboboxSelected>>", self.search_by_order_type)
        self.search_order_type.place(x=1195, y=20)

        # Table
        self.table = Table(
            self.window,
            ["Id", "Order Type", "Customer", "Employee", "Date & Time", "Payment Id", "Ware Trans Id", "Tax",
             "Total Discount", "Total Amount"],
            [40, 90, 140, 140, 150, 90, 90, 90, 90, 120],
            280, 60,
            21,
            self.select_from_table
        )

        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=475)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=97, y=475)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=175, y=475)
        Button(self.window, text="View Order", width=18, command=self.order_item_view).place(x=20, y=435)
        Button(self.window, text="Refresh", width=7, command=self.refresh).place(x=175, y=435)

        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = OrderController.save(self.order_type.get(), self.customer_id.get(), self.employee_id.get(),
                                               self.date_time.get(), self.payment_id.get(),
                                               self.warehouse_transaction_id.get(), self.tax.get(),
                                               self.total_discount.get(), self.total_amount.get())
        if status:
            messagebox.showinfo("Order Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Order Save Error", message)

    def edit_click(self):
        status, message = OrderController.update(self.order_id.get(), self.order_type.get(), self.customer_id.get(),
                                                 self.employee_id.get(),
                                                 self.date_time.get(), self.payment_id.get(),
                                                 self.warehouse_transaction_id.get(),
                                                 self.tax.get(), self.total_discount.get(), self.total_amount.get())
        if status:
            messagebox.showinfo("Order Update", message)
            self.reset_form()
        else:
            messagebox.showerror("Order Update Error", message)

    def delete_click(self):
        status, message = OrderController.delete(self.order_id.get())
        if status:
            messagebox.showinfo("Order Delete", message)
            self.reset_form()
        else:
            messagebox.showerror("Order Delete Error", message)

    def order_item_view(self):
        if self.order_id.get():
            status, Session.order_items = OrderItemController.find_by_order_id(self.order_id.get())
            if status:
                # order_item = OrderItem(*Session.order_items[0].__dict__.values())
                print(Session.order_items)
                ui = ShowOrderView()
                ui.table.refresh_table(Session.order_items)
            else:
                messagebox.showerror("Order Item View Error", "No Order Item Found")
        else:
            messagebox.showerror("Select", "Select Order")

    def reset_form(self):
        self.order_id.clear()
        self.customer_id.clear()
        self.employee_id.clear()
        self.date_time.clear()
        self.payment_id.clear()
        self.warehouse_transaction_id.clear()
        self.tax.clear()
        self.total_discount.clear()
        self.total_amount.clear()
        self.order_type.set("Basket")
        status, order_list = OrderController.find_all()
        self.table.refresh_table(order_list)

    def select_from_table(self, selected_order):
        if selected_order:
            status, order = OrderController.find_by_id(selected_order[0])
            if status:
                order = Order(*selected_order)
                self.order_id.set(order.order_id)
                self.order_type.set(order.order_type)
                self.customer_id.set(order.customer_id)
                self.employee_id.set(order.employee_id)
                self.date_time.set(order.date_time)
                self.payment_id.set(order.payment_id)
                self.warehouse_transaction_id.set(order.warehouse_transaction_id)
                self.tax.set(order.tax)
                self.total_discount.set(order.total_discount)
                self.total_amount.set(order.total_amount)

    def search_by_customer_id(self):
        status, order_list = OrderController.find_by_customer_id(self.search_customer_id.get())
        if status and order_list:
            self.table.refresh_table(order_list)
        else:
            self.reset_form()

    def search_by_employee_id(self):
        status, order_list = OrderController.find_by_employee_id(self.search_employee_id.get())
        if status and order_list:
            self.table.refresh_table(order_list)
        else:
            self.reset_form()

    def search_by_date_time_range(self, event):
        status, order_list = OrderController.find_by_date_time_range(self.search_start_date_time.get(),
                                                                     self.search_end_date_time.get())
        if status and order_list:
            self.table.refresh_table(order_list)
        else:
            self.reset_form()

    def search_by_order_type(self, event):
        status, order_list = OrderController.find_by_order_type(self.search_order_type.get())
        if status and order_list:
            self.table.refresh_table(order_list)
        else:
            self.reset_form()

    def refresh(self):
        self.reset_form()

# TODO: Why order_item_view (line 135) doesn't populate the table??
# TODO: Why date selection in "Start Date" and "End Date" is not repeatable?
# TODO: Why table is not refreshed after each search?
# TODO: In "Save" and "Update", How to enter Customer and Employee Name (NOT Id)
#           and get the Ids automatically?
