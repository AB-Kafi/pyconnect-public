import tkinter as tk


class Post(tk.Frame):
     def __init__(self,root,app):
        tk.Frame.__init__(self, root)
        self.config(bg = 'white')
        self.data = tk.Text(self, height=4, width=45, border = 1)
        self.data.place(x = 70, y = 350)
        self.data.config(bg = "white")
        self.postbutton = tk.Button(self, text = 'post' ,width = 7, height =2 , border = 0, command = app.postnow )
        self.postbutton.place(x= 200, y = 430)
        


if __name__ ==  "__main__":
    root = tk.Tk()
    post = Post(root,None)
    root.geometry("480x720")
    post.pack(fill = "both", expand = 1)
    
    root.mainloop()
