from view import *
from controller import EmployeeController
from model import Session

class LoginView:
    def __init__(self):
        self.employee_controller = EmployeeController()
        self.window=Tk()
        self.window.title("Employee")
        self.window.config(background="white")
        self.window.geometry("300x500")

        image = Image.open("./view/images/user.png")
        image = ImageTk.PhotoImage(image)

        Label(self.window, image=image).place(x=50, y=15)

        self.username = LabelWithEntry(self.window,"Username",30,270)
        self.password = LabelWithEntry(self.window,"Password",30,310)

        self.username.set("aliuser")
        self.password.set("pass1234")

        Button(self.window, text="Login", width=8,font=("Arial", 14), command=self.login).place(x=50, y=380, width=200,height=70)

        self.window.mainloop()


    def login(self):
        status, employee = self.employee_controller.find_by_username_and_password(self.username.get(), self.password.get())

        if status:
            self.window.destroy()
            Session.employee = employee
            DashboardView()
        else:
            messagebox.showerror("Login Error", "Access Denied !!!")

