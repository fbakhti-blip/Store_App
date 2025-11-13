from view import *
from model import Delivery, Session
from controller import DeliveryController


class DeliveryView:
    def __init__(self):

        self.window = Tk()
        self.window.geometry("850x320")
        self.window.title("Delivery")

        self.delivery_id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.first_name = LabelWithEntry(self.window, "First Name", 20, 60)
        self.last_name = LabelWithEntry(self.window, "Last Name", 20, 100)
        self.address = LabelWithEntry(self.window, "Address", 20, 140)
        self.description = LabelWithEntry(self.window, "Description", 20, 180)

        self.search_first_name = LabelWithEntry(self.window, "First Name", 270, 20, distance=70,
                                                on_keypress_function=self.search_by_fullname)
        self.search_last_name = LabelWithEntry(self.window, "Last Name", 480, 20, distance=70,
                                               on_keypress_function=self.search_by_fullname)

        self.table = Table(
            self.window,
            ["Id", "First Name", "Last Name", "Address", "Description"],
            [40, 100, 100, 140, 160],
            270, 60,
            10,
            self.select_from_table
        )

        Button(self.window, text="Select Delivery", width=19, command=self.select_delivery).place(x=20, y=220)
        Button(self.window, text="Refresh", width=7, command=self.reset_form).place(x=180, y=220)
        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=260)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=260)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=260)

        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = DeliveryController.save(self.first_name.get(), self.last_name.get(), self.address.get(),
                                                  self.description.get())
        if status:
            messagebox.showinfo("Delivery Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Delivery Save Error", message)

    def edit_click(self):
        status, message = DeliveryController.update(self.delivery_id.get(), self.first_name.get(), self.last_name.get(),
                                                    self.address.get(), self.description.get())
        if status:
            messagebox.showinfo("Delivery Update", message)
            self.reset_form()
        else:
            messagebox.showerror("Delivery Update Error", message)

    def delete_click(self):
        status, message = DeliveryController.delete(self.delivery_id.get())
        if status:
            messagebox.showinfo("Delivery Delete", message)
            self.reset_form()
        else:
            messagebox.showerror("Delivery Delete Error", message)

    def reset_form(self):
        self.delivery_id.clear()
        self.first_name.clear()
        self.last_name.clear()
        self.address.clear()
        self.description.clear()
        self.search_first_name.clear()
        self.search_last_name.clear()
        status, delivery_list = DeliveryController.find_all()
        self.table.refresh_table(delivery_list)

    def select_from_table(self, selected_delivery):
        if selected_delivery:
            status, delivery = DeliveryController.find_by_id(selected_delivery[0])
            if status:
                delivery = Delivery(*selected_delivery)
                self.delivery_id.set(delivery.delivery_id)
                self.first_name.set(delivery.first_name)
                self.last_name.set(delivery.last_name)
                self.address.set(delivery.address)
                self.description.set(delivery.description)

    def search_by_fullname(self):
        status, delivery_list = DeliveryController.find_by_firstname_and_lastname(self.search_first_name.get(),
                                                                                  self.search_last_name.get())
        if status and delivery_list:
            self.table.refresh_table(delivery_list)
        else:
            messagebox.showerror("Error", "Person Not Found")

    def select_delivery(self):
        if self.delivery_id.get():
            status, Session.delivery = DeliveryController.find_by_id(self.delivery_id.get())
        else:
            messagebox.showerror("Select", "Select Delivery")

    def refresh(self):
        pass
