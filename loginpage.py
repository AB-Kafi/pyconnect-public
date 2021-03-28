import tkinter as tk
from tkinter import ttk
from ImageAdapter import ImageAdapter


class Login(tk.Canvas):
    def __init__(self, root, app):
        tk.Canvas.__init__(self, root, width=480, height=720)

        self.adapter = ImageAdapter()
        self.login = self.adapter.convert(
            'login/LoginPage.png', size=[480, 720])
        self.background = self.login
        self.background = self.create_image(
            0, 0, anchor=tk.NW, image=self.login)

        # text field
        self.email = tk.Entry(root, show=None)
        self.email.config(bg='white')
        self.password = tk.Entry(root, show='*')
        self.password.config(bg='white')
        self.create_window(240, 450, window=self.email)
        self.create_window(240, 500, window=self.password)

        # button
        # login
        phtot = tk.PhotoImage(file="Assets/Login.png")
        self.loginimage = phtot.subsample(3, 3)
        self.loginbutton = tk.Button(
            self, image=self.loginimage, width=109, height=30, border=0, command = app.loginpressed )
        self.buttonwindow = self.create_window(
            180, 550, anchor=tk.NW, window=self.loginbutton)


if __name__ == "__main__":
    root = tk.Tk()
    Log = Login(root, None)
    Log.pack()
    root.geometry('480x720')
    root.resizable(False, False)
    root.mainloop()
