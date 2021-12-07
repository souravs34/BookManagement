from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)
     
def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),ISBN_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),ISBN_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),ISBN_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),ISBN_text.get())
    
# This wraps whole frontend-app
window =Tk()

window.wm_title("Library Management System")



l1 = Label(window,text="Book Name",font=('Helvetica', 10, 'bold'),bg='black',foreground="yellow")
l1.grid(row=0,column=0)


l2 = Label(window,text="Author Name",font=('Helvetica', 10, 'bold'),bg='black',foreground="yellow")
l2.grid(row=0,column=2)

l3 = Label(window,text="Year",font=('Helvetica', 10, 'bold'),bg='black',foreground="yellow")
l3.grid(row=1,column=0)


l3 = Label(window,text="Unique Id",font=('Helvetica', 10, 'bold'),bg='black',foreground="yellow")
l3.grid(row=1,column=2)
title_text=StringVar()
e1 = Entry(window,textvariable=title_text,)
e1.grid(row=0,column=1)

author_text=StringVar()
e2 = Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)
ISBN_text=StringVar()
e4 = Entry(window,textvariable=ISBN_text)
e4.grid(row=1,column=3)
year_text=StringVar()
e3 = Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)



list1 = Listbox(window,height=6,width=30)
list1.grid(row=2,column=0,rowspan=12,columnspan=2)


#createscrollbar inside in the listbox
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=12)
 
#create the actions of the scrollbar
list1.configure(yscrollcommand=sb1) #place the scrollbar in the y axis (sb1 inside list 1)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)


b1=Button(window,text="View All Books",width=20,font=('Helvetica', 10, 'bold'),bg='black',activebackground='grey',foreground="yellow",command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Book",bg='black',font=('Helvetica', 10, 'bold'),activebackground='grey',foreground="yellow",width=20,command=search_command)
b2.grid(row=4,column=3)

b3=Button(window,text="Add Book",bg='black',font=('Helvetica', 10, 'bold'),activebackground='grey',foreground="yellow",width=20,command=add_command)
b3.grid(row=6,column=3)

b4=Button(window,text="Update Book Data",font=('Helvetica', 10, 'bold'),bg='black',activebackground='grey',foreground="yellow",width=20,command=update_command)
b4.grid(row=8,column=3)

b5=Button(window,text="Delete Book",font=('Helvetica', 10, 'bold'),bg='black',activebackground='grey',foreground="yellow",width=20,command=delete_command)
b5.grid(row=10,column=3)

b6=Button(window,text="Close Window",font=('Helvetica', 10, 'bold'),bg='black',activebackground='grey',foreground="yellow",width=20,command=window.destroy)
b6.grid(row=12,column=3)

window.mainloop()