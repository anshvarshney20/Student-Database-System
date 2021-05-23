from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import csv

import os
global uno,name,clas,persent,win

def delete():
    global uno,name,clas,persent,win
    u=uno.get()
    n=name.get()
    c=clas.get()
    p=persent.get()
    count=1
    data=[]
    file=open("main.csv")
    reader=csv.reader(file,delimiter=",")
    for row in reader:
        if int(row[0])==int(u):
            pass
        elif int(row[0])!=int(u):
            data.append([count,row[1],row[2],row[3]])
            count+=1
    file.close()
    file=open("main.csv","w")
    writer=csv.writer(file,delimiter=",",lineterminator="\n")
    writer.writerows(data)
    file.close()
    messagebox.showinfo("Student Database Management","Record Deleted Sucessfully")
    win.geometry("350x80")
    uno.set("Select U.No.")
def find():
    global uno,name,clas,persent
    u=uno.get()
    if u=="Select U.No.":
        messagebox.showinfo("Find","Please Select U.No.")
    elif len(u)>0 :
        file=open("main.csv")
        reader=csv.reader(file,delimiter=",")
        for row in reader:
            
            if int(u)==int(row[0]):
                win.geometry("350x250")
                name.set(row[1])
                clas.set(row[2])
                persent.set(row[3])
        file.close()
def press(e):
    global uno,name,clas,persent
    u=uno.get()
    if u=="Select U.No.":
        messagebox.showinfo("Student Database Management","Please Select U.No.")
    if repr(e.keycode)==67:
        close()
    elif len(u)>0 :
        if repr(e.keysym)=="'Return'":
            find()
    else:
        messagebox.showinfo("Student Database Management","Please Select U.No.")
def main():
    global uno,name,clas,persent,win
    win=Tk()
    win.title(" Delete Record")
    win.geometry("350x80")
    win.config(bg="white")
    win.resizable(0,0)
    win.iconbitmap("lite.ico")
    uno=StringVar()
    name=StringVar()
    clas=StringVar()
    persent=StringVar()
    data=[]
    Label(win,text="Delete Record",bg="white",fg="black",font=("Georgia",16)).place(x=108,y=2)
    Label(win,text="U.No.",bg="white",fg="black",font=("Georgia",12)).place(x=30,y=50)
    Label(win,text="Name",bg="white",fg="black",font=("Georgia",12)).place(x=30,y=90)
    Label(win,text="Class",bg="white",fg="black",font=("Georgia",12)).place(x=30,y=130)
    Label(win,text="Hg No.",bg="white",fg="black",font=("Georgia",12)).place(x=30,y=170)
    file=open("main.csv")
    read=csv.reader(file,delimiter=",")
    for row in read:
        data.append(row[0])
        
    e0=ttk.OptionMenu(win,uno,"Select U.No.",*data)
    e0.place(x=140,y=50)
    e0.focus()
    e1=Entry(win,textvariable=name,state="disable")
    e1.place(x=140,y=90)
    e1.focus()
    e2=Entry(win,textvariable=clas,state="disable")
    e2.place(x=140,y=130)
    e3=Entry(win,textvariable=persent,state="disable")
    e3.place(x=140,y=170)
    Button(win,text="Find",bg="yellow",fg="red",font=("Georgia",9),command=find).place(x=290,y=47)
    Button(win,text="Delete",bg="yellow",fg="red",font=("Georgia",9),command=delete).place(x=150,y=200)
    win.bind("<Key>",press)
    win.mainloop()
    
if __name__=="__main__":
    main()
