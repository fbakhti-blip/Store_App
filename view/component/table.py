from tkinter import *
import tkinter.ttk as ttk


class Table:
    def table_select(self, event):
        row_id = self.table.focus()
        item = self.table.item(row_id)["values"]
        self.function_name(item)

    def clear_table(self):
        for item in self.table.get_children():
            self.table.delete(item)

    def refresh_table(self, data_list):
        self.clear_table()
        if data_list:
            for data in data_list:
                self.table.insert("", END, values=data.to_tuple())

    def __init__(self, window, headings, column_widths, x, y, height=10, function_name=None):
        self.function_name = function_name
        columns = list(range(len(headings)))

        self.table = ttk.Treeview(window, columns=columns, height=height, show="headings")

        for col in columns:
            self.table.heading(col, text=headings[col])
            self.table.column(col, width=column_widths[col])

        # Calculate scrollbar position (to the right of the table)
        scrollbar_x = x + sum(column_widths)

        self.table.place(x=x, y=y)

        # Get the actual height of the treeview
        table_height = self.table.winfo_reqheight()

        # Create vertical scrollbar with matching height
        self.scrollbar = ttk.Scrollbar(window, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(x=scrollbar_x, y=y, height=table_height)

        self.table.bind("<<TreeviewSelect>>", self.table_select)
