import tkinter as tk
from tkinter import ttk
from ImageAdapter import ImageAdapter

class Signup(tk.Canvas):
    def __init__(self, parent, app): 
        tk.Canvas.__init__(self, parent, width = 480, height = 720)
        
        self.adapter = ImageAdapter()        
        self.login = self.adapter.convert('login/LoginPage.png', size = [480,720])
        self.background = self.login
        self.background = self.create_image(0,0, anchor = tk.NW, image = self.login) 

        #text field
        self.email = tk.Entry(parent, show = None)
        self.password = tk.Entry(parent, show = '*')
        self.create_window(240, 450, window = self.email)
        self.create_window(240, 500, window = self.password)

        #button
        #login
        phtot = tk.PhotoImage(file ="Assets/signup.png")
        self.signupimage = phtot.subsample(3,3)
        self.signupbutton = tk.Button(self,image = self.signupimage ,width = 110, height =30 , border = 0 )
        self.buttonwindow = self.create_window(180,550, anchor = tk.NW, window = self.signupbutton )

if __name__ == "__main__":
    root = tk.Tk()
    Log =Signup(root,None)
    Log.pack()
    root.geometry('480x720')
    root.resizable(False,False)
    root.mainloop()