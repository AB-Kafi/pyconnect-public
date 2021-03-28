from database import CursorFromConnectionPool

class Postinfo:
    def __init__(self, postid, userid, posttext, likecount):
        self.postid = postid
        self.userid = userid
        self.posttext = posttext
        self.likecount = likecount
     
    @classmethod
    def load_from_db(cls):
        with CursorFromConnectionPool() as cursor:
            cursor.execute('SELECT * FROM posts')
            return cursor.fetchall()
          

    def save_to_db(self):
        with CursorFromConnectionPool() as cursor:
            cursor.execute('insert into posts(userid,posttext) values(%s,%s)',(self.userid,self.posttext))
    