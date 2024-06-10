from tkinter import *
from tkinter import messagebox
import datadb
root = Tk()
root.title('UI_db')
root.geometry('600x400')
root.resizable(False , False)
db1 = datadb.Database('d:/myfile1.db')
def insert():
    if len(ent_fname.get()) == 0  or len(ent_lname.get()) == 0:
           messagebox.showerror('EROR' , 'fristname and lastname empty')
           return
    db1.insert(ent_fname.get(),ent_lname.get(),ent_city.get(),ent_tel.get())
    clear()
    ent_fname.focus()
    select()
def select_item(event):
    try:
        global selected_item
        
        index = lst.curselection()
        selected_item = lst.get(index)
        # record = selected_item.split(',')
        # a = str(selected_item)
        # record = select_item.split(',')
        ent_fname.delete(0 , END)
        ent_fname.insert(END, selected_item[1])
        ent_lname.delete(0 , END)
        ent_lname.insert(END , selected_item[2])
        ent_city.delete(0 , END)
        ent_city.insert(END, selected_item[3])
        ent_tel.delete(0 , END)
        ent_tel.insert(END , selected_item[4])     
    except IndexError:
        pass
def listt():
    lst.delete(0 , END)
    for row in db1.select():
        lst.insert(END , f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}')        
def select():
    lst.delete(0,END)
    records=db1.select()
    for record in records:
        lst.insert(END,record)
def clear():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_city.delete(0,END)
    ent_tel.delete(0,END)
    ent_fname.focus()
def delete():
    index = lst.curselection()
    data = lst.get(index)
    db1.delete(data[0])
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_city.delete(0,END)
    ent_tel.delete(0,END)
    ent_fname.focus()
    select()
def Exit():
    result = messagebox.askquestion('exit' , 'do you want to go out?')
    if result == 'yes':
        root.destroy()
def update():
    db1.update(selected_item[0], ent_fname.get(), ent_lname.get(), ent_city.get(), ent_tel.get())
    listt()
    
def search():
     x = (ent_search.get())
     record = db1.search(x)
     if len(record) == 0:
         messagebox.showeror('Eror' , 'Record not found')
         return
     lst.delete(0,END)
     lst.insert(0,record)
     ent_search.delete(0,END)
     ent_search.focus()




#________Label____________
lbl_fname = Label(root , text='Fname:  ')
lbl_Lname = Label(root , text='Lname:  ')
lbl_city = Label(root , text='City:  ')
lbl_tel = Label(root , text='Tel:  ')
lbl_fname.place(x=10,y=10)
lbl_Lname.place(x=10,y=50)
lbl_city.place(x=330,y=10)
lbl_tel.place(x=330,y=50)
#________Entry__________
fname_text = StringVar()
lname_text = StringVar()
city_text = StringVar()
tel_text = StringVar()
Search_text = StringVar()
ent_fname = Entry(root , textvariable=fname_text.get())
ent_lname = Entry(root , textvariable=lname_text.get())
ent_city = Entry(root , textvariable=city_text.get())
ent_tel = Entry(root , textvariable=tel_text.get())
ent_search = Entry(root , textvariable=Search_text.get())
ent_fname.place(x=110,y=10)
ent_lname.place(x=110,y=50)
ent_city.place(x=440,y=10)
ent_tel.place(x=440,y=50)
ent_search.place(x=430,y=170)
#________Listbox_____
lst = Listbox(root,width=90,height=10)
lst.place(x=10,y=210)
#_______Button______
btn_insert = Button(root , text='Insert' , width=10,height=2,command=insert)
btn_update = Button(root , text='Update' , width=10,height=2 , command=update)
btn_show = Button(root , text='Show' , width=10,height=2,command=select)
btn_clear = Button(root , text='Clear' , width=10,height=2 , command = clear)
btn_delete = Button(root , text='Delete' , width=10,height=2,command=delete)
btn_exit = Button(root , text='Exit' , width=10,height=2,command=Exit)
btn_search = Button(root , text = 'Search', width=10,height=2 , command=search)
btn_insert.place(x=10,y=100)
btn_show.place(x=10,y=160)
btn_delete.place(x=160,y=100)
btn_clear.place(x=160,y=160)
btn_update.place(x=310,y=100)
btn_exit.place(x=310,y=160)
btn_search.place(x=460,y=100)


#________________

lst.bind('<<ListboxSelect>>' , select_item)






root.mainloop()