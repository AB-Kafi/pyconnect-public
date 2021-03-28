import tkinter as tk
from startpage import Start
from loginpage import Login
from signuppage import Signup
from homepage import Home
import time
from database import Database
from user import User
from post import Postinfo
from postpage import Post


class App:
    def __init__(self, root):
        # database init
        self.root = root
        Database.initialise(database="project", user="postgres", password="1234", host="localhost")
        self.user = None 
        self.postdata = Postinfo.load_from_db()

        self.startframe = tk.Frame(root)
        self.loginframe = tk.Frame(root)
        self.signupframe= tk.Frame(root)


        self.startpage = Start(self.startframe,self)
        self.startpage.pack()
        
        self.login = Login(self.loginframe,self)
        self.login.pack()
        
        self.home = Home(root,self) #it needs to be packed in function
        self.postpage = Post(root,self)
       
        
    def clear(self,item):
       item.destroy()   
    
    def loginpressed(self):
        email = self.login.email.get()
    
        password = self.login.password.get()
      
        self.user = User.load_from_db(email,password)
       
        print(self.user.userid)
        if self.user != None:
            if  self.user.password == password:
                self.clear(self.loginframe)
                self.home.pack(expand = 1, fill = 'both')
            else:
                print("User not found")
        else:
            print("User None returned")
        
        

       
    def startlogin(self):
        self.clear(self.startframe)
        self.loginframe.pack(fill = 'both', expand = 1)

    def showstart(self):
        self.startframe.pack()
    
    def showhome(self):
        self.clear(self.postpage)
        self.postdata = Postinfo.load_from_db()
        self.home = Home(self.root,self)
        self.home.pack(fill = 'both', expand = 1)
        self.postpage = Post(self.root,self)


    def showaddpost(self):
        self.clear(self.home)
        self.postpage.pack(fill = 'both', expand = 1)

     
    def run(self):
        if self.user == None:
            self.showstart()
        else:
            self.home.pack(fill = "both", expand = 1)

    def postnow(self):
        data = self.postpage.data.get("1.0",'end-1c')
        post = Postinfo(None,self.user.userid,data,None)
        post.save_to_db()
        self.showhome()


       



if __name__ == '__main__':
    root = tk.Tk()
    root.title('Pyconnect')
    root.geometry('480x720')
    root.resizable(False, False)
    app = App(root)
    app.run()
    root.mainloop()
