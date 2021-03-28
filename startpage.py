import tkinter as tk
from tkinter import ttk
from ImageAdapter import ImageAdapter
from loginpage import Login

class Start(tk.Canvas):
    def __init__(self, parent, app): 
        tk.Canvas.__init__(self, parent, width = 480, height = 720)
        
        self.adapter = ImageAdapter()        
        self.login = self.adapter.convert('login/LoginPage.png', size = [480,720])
        self.background = self.login
        self.background = self.create_image(0,0, anchor = tk.NW, image = self.login) 
        
        #button
        #login
        phtot = tk.PhotoImage(file ="Assets/Login.png")
        self.loginimage = phtot.subsample(3,2)
        self.loginbutton = tk.Button(self,image = self.loginimage ,width = 110, height =50 , border = 0, command=app.startlogin )
        self.buttonwindow = self.create_window(100,500, anchor = tk.NW, window = self.loginbutton )
        #signup
        phtot = tk.PhotoImage(file ="Assets/signup.png")
        self.signupimage = phtot.subsample(3,2)
        self.signupbutton = tk.Button(self,image = self.signupimage ,width = 110, height =50 , border = 0 )
        self.buttonwindow2 = self.create_window(230,500, anchor = tk.NW, window = self.signupbutton )


if __name__ == "__main__":
    root = tk.Tk()
    Log = Start(root, None)
    Log.pack()
    root.geometry('480x720')
    root.resizable(False,False)
    root.mainloop()