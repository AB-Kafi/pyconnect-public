from database import CursorFromConnectionPool

class User:
    def __init__(self, userid = None, email= None, password= None):
        self.userid = userid
        self.email = email
        self.password = password
    
    @classmethod
    def load_from_db(cls, email, password):
        with CursorFromConnectionPool() as cursor:
            cursor.execute('SELECT * FROM users WHERE email = %s',(email,))
            user_data = cursor.fetchone()
            if user_data != None:
                print(user_data)
                return cls(userid = user_data[0], email = user_data[1], password = user_data[2])
            else:
                return None
    def save_to_db(self):
        with CursorFromConnectionPool as cursor:
            cursor.execute('insert into users (email,password) values(%s,%s)',(self.email,self.password))
    