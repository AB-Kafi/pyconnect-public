import tkinter as tk
from tkinter import ttk



class Buttonframe():
    def __init__(self,root, x, y, app):
        fm = tk.Frame(root,width=500,height=500)
       
       
   
       # home = tk.Button(fm, text = 'home' ,width = 5, height =2 , border = 0, bg = "white", command = app.showhome )
        add = tk.Button(fm, text = 'add' ,width = 5, height =2 ,bg = "white", border = 0,command = app.showaddpost )


       # home.grid(row = 1,column = 0, padx = 2)
        add.grid(row = 1,column = 2, padx = 2)
        fm.place(x = x, y = y)
    
    


if __name__ == '__main__':
    root = tk.Tk()
    
    root.geometry('480x700')
    Buttonframe(root,200, 300,none)
    root.resizable(False,False)
    root.mainloop()