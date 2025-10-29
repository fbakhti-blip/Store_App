from view import *
from model import Product, Session
from controller import ProductController


class ProductView:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1000x440")
        self.window.title("product")

        self.product_id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.name = LabelWithEntry(self.window, "Name", 20, 60)
        self.brand = LabelWithEntry(self.window, "Brand", 20, 100)
        self.model = LabelWithEntry(self.window, "Model", 20, 140)
        self.serial = LabelWithEntry(self.window, "Serial", 20, 180)
        self.category = LabelWithEntry(self.window, "Category", 20, 220)
        self.unit = LabelWithEntry(self.window, "Unit", 20, 260)
        self.expiration_date = LabelWithEntry(self.window, "ExpirationDate", 20, 300)

        self.search_name = LabelWithEntry(self.window, "Name", 270, 20, distance=60,
                                          on_keypress_function=self.search_name_brand)
        self.search_brand = LabelWithEntry(self.window, "Brand", 500, 20, distance=60,
                                           on_keypress_function=self.search_name_brand)

        self.table = Table(
            self.window,
            ["Id", "Name", "Brand", "Model", "Serial", "Category", "Unit", "ExpirationDate"],
            [40, 100, 100, 60, 100, 100, 100, 100],
            270, 60,
            16,
            self.select_from_table
        )

        Button(self.window, text="Select Product", width=19, command=self.select_product).place(x=20, y=340)
        Button(self.window, text="Refresh", width=7, command=self.refresh).place(x=180, y=340)
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
        self.expiration_date.clear()
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
            self.expiration_date.set(product.expiration_date)

    def search_name_brand(self):
        status, product_list = ProductController.find_by_name_and_brand(self.search_name.get(), self.search_brand.get())
        if status and product_list:
            self.table.refresh_table(product_list)

    def select_product(self):
        if self.product_id.get():
            status, Session.product = ProductController.find_by_id(self.product_id.get())
        else:
            messagebox.showerror("Select", "Select Product")

    def refresh(self):
        pass
