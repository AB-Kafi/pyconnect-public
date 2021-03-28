import tkinter as tk
from tkinter import ttk
from buttonframe import Buttonframe

class Home(tk.Frame):
    def __init__(self,root, app):
        tk.Frame.__init__(self, root)
        #main_frame = tk.Frame(root)
        #main_frame.pack(fill = 'both', expand = 1)

        my_canvas= tk.Canvas(self, height = 600)
        my_canvas.pack(side = 'left', fill = tk.X, expand = 1)
       
        my_scrollbar = ttk.Scrollbar(self, orient = 'vertical' ,command  = my_canvas.yview)
        my_scrollbar.pack(side = 'right', fill = 'y')

        my_canvas.configure(yscrollcommand = my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox('all')))
        sec_frame = tk.Frame(my_canvas)

        my_canvas.create_window((0,0), window = sec_frame, anchor = "nw")
        Buttonframe(self, 170, 650,app)
        #tk.Label(buttonframe, text = 'this is button frame').pack()
      

        for num,things in enumerate(app.postdata):
           tk.Label(sec_frame, text = f'{things[2]}', bg = "white").grid(row = num, column = 0, pady =10, padx = 10)
           

if __name__ == "__main__":
    root = tk.Tk()
   
    root.geometry("480x720")
    root.resizable(False,False)
    x = Home(root,None)
    x.pack(fill = 'both', expand = 1)

    root.mainloop()