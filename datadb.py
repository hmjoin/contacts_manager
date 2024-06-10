import sqlite3
class Database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute('''
                         CREATE TABLE if not exists contacts(id integer primary key,fname text,lname text,
                         city text,tel integer)
                         ''')
        self.con.commit()
    def insert(self,fname,lname,city,tel):
        self.cur.execute('INSERT INTO contacts(id,fname,lname,city,tel) VALUES (null,?,?,?,?)'
                         ,(fname,lname,city,tel))
        self.con.commit()
        print('insert record')
        
    def select(self):
        self.cur.execute('SELECT * from contacts')
        records = self.cur.fetchall()
        return records
    def delete(self,id):
        self.cur.execute('DELETE from contacts where id =?',(id,))
        self.con.commit()
    def update(self,id,fname,lname,city,tel):
        self.cur.execute('''
                         UPDATE contacts SET fname =? ,Lname =?, city=?, tel =? WHERE id=?
                         ''' , (fname , lname , city , tel , id))
        self.con.commit()
    def search(self , input_):
        self.cur.execute('''
                         SELECT * FROM contacts WHERE id =? or fname =? or lname =? 
                         or city =? or tel =?
                         ''' , (input_,input_,input_,input_,input_))
        return self.cur.fetchall()
        
        
        
        
        
        