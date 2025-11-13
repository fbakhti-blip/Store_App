from view import *
from tkcalendar import *
from model import Product, Session
from controller import ProductController


class ProductView:
    def __init__(self):

        self.window = Tk()
        self.window.geometry("1000x440")
        self.window.title("Product")

        self.product_id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.name = LabelWithEntry(self.window, "Name", 20, 60)
        self.brand = LabelWithEntry(self.window, "Brand", 20, 100)
        self.model = LabelWithEntry(self.window, "Model", 20, 140)
        self.serial = LabelWithEntry(self.window, "Serial", 20, 180)
        self.category = LabelWithEntry(self.window, "Category", 20, 220)
        self.unit = LabelWithEntry(self.window, "Unit", 20, 260)

        Label(self.window, text="ExpirationDate").place(x=20, y=300)
        self.expiration_date = DateEntry(self.window, width=17, selectmode="day", date_pattern="y/mm/dd")
        self.expiration_date.place(x=110, y=300)

        self.search_name = LabelWithEntry(self.window, "Name", 270, 20, distance=40,
                                          on_keypress_function=self.search_name_brand)
        self.search_brand = LabelWithEntry(self.window, "Brand", 450, 20, distance=40,
                                           on_keypress_function=self.search_name_brand)

        # Search by Expiry Date
        Label(self.window, text="Expiry Date").place(x=630, y=20)
        self.search_expiry_date = DateEntry(self.window, width=16, selectmode="day", date_pattern="y/mm/dd")
        self.search_expiry_date.bind("<<DateEntrySelected>>", self.search_by_expiry_date)
        self.search_expiry_date.place(x=700, y=20)

        self.table = Table(
            self.window,
            ["Id", "Name", "Brand", "Model", "Serial", "Category", "Unit", "ExpirationDate"],
            [40, 100, 100, 80, 80, 100, 100, 100],
            270, 60,
            16,
            self.select_from_table
        )

        Button(self.window, text="Select Product", width=19, command=self.select_product).place(x=20, y=340)
        Button(self.window, text="Refresh", width=7, command=self.reset_form).place(x=180, y=340)
        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=380)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=380)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=380)

        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = ProductController.save(self.name.get(), self.brand.get(), self.model.get(),
                                                 self.category.get(),
                                                 self.serial.get(), self.unit.get(), self.expiration_date.get())
        if status:
            messagebox.showinfo("Product Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Product Save Error", message)

    def edit_click(self):
        status, message = ProductController.update(self.product_id.get(), self.name.get(), self.brand.get(),
                                                   self.model.get(),
                                                   self.category.get(), self.serial.get(), self.unit.get(),
                                                   self.expiration_date.get())
        if status:
            messagebox.showinfo("Product Update", message)
            self.reset_form()
        else:
            messagebox.showerror("Product Update Error", message)

    def delete_click(self):
        status, message = ProductController.delete(self.product_id.get())
        if status:
            messagebox.showinfo("Product Delete", message)
            self.reset_form()
        else:
            messagebox.showerror("Product Delete Error", message)

    def reset_form(self):
        self.product_id.clear()
        self.name.clear()
        self.brand.clear()
        self.model.clear()
        self.category.clear()
        self.serial.clear()
        self.unit.clear()
        self.expiration_date.set_date(None)
        self.search_name.clear()
        self.search_brand.clear()
        self.search_expiry_date.set_date(None)
        status, product_list = ProductController.find_all()
        self.table.refresh_table(product_list)

    def select_from_table(self, selected_product):

        if selected_product:
            product = Product(*selected_product)
            self.product_id.set(product.product_id)
            self.name.set(product.name)
            self.brand.set(product.brand)
            self.model.set(product.model)
            self.category.set(product.category)
            self.unit.set(product.unit)
            self.serial.set(product.serial)
            self.expiration_date.set_date(product.expiration_date)

    def search_name_brand(self):
        status, product_list = ProductController.find_by_name_and_brand(self.search_name.get(), self.search_brand.get())
        if status and product_list:
            self.table.refresh_table(product_list)
        else:
            messagebox.showerror("Error", "Product Not Found")

    def search_by_expiry_date(self, event):
        status, product_list = ProductController.find_by_expire_date_until(self.search_expiry_date.get())
        if status and product_list:
            self.table.refresh_table(product_list)
        else:
            self.reset_form()

    def select_product(self):
        if self.product_id.get():
            status, Session.product = ProductController.find_by_id(self.product_id.get())
        else:
            messagebox.showerror("Select", "Select Product")

    def refresh(self):
        pass
