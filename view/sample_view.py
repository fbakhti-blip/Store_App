from view import *
from model import Sample
from controller import SampleController


class SampleView:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("840x320")
        self.window.title("Sample")

        self.sample_id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.name = LabelWithEntry(self.window, "Name", 20, 60)
        self.description = LabelWithEntry(self.window, "Description", 20, 100)

        self.table = Table(
            self.window,
            ["Id", "Name", "Description"],
            [40, 200, 300],
            270, 20,
            12,
            self.select_from_table
        )

        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=260)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=260)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=260)
        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = SampleController.save(self.name.get(), self.description.get())
        if status:
            messagebox.showinfo("Sample Saved", message)
            self.reset_form()
        else:
            messagebox.showerror("Sample Save Error", message)

    def edit_click(self):
        status, message = SampleController.update(self.sample_id.get(), self.name.get(), self.description.get())
        if status:
            messagebox.showinfo("Sample Updated", message)
            self.reset_form()
        else:
            messagebox.showerror("Sample Update Error", message)

    def delete_click(self):
        status, message = SampleController.delete(self.sample_id.get())
        if status:
            messagebox.showinfo("Sample Deleted", message)
            self.reset_form()
        else:
            messagebox.showerror("Sample Delete Error", message)

    def reset_form(self):
        self.sample_id.clear()
        self.name.clear()
        self.description.clear()
        status, sample_list = SampleController.find_all()
        self.table.refresh_table(sample_list)

    def select_from_table(self, selected_sample):
        if selected_sample:
            status, sample = SampleController.find_by_id(selected_sample[0])
            if status:
                sample = Sample(*selected_sample)
                self.sample_id.set(sample.sample_id)
                self.name.set(sample.name)
                self.description.set(sample.description)
