from tkinter import *
import csv
import os
from PIL import ImageTk
file=open("main.csv","a")
file.close()
def close():
    win.destroy()
def credit():
    os.system("python credits.py")
def edit():
    os.system("python edit.py")
def delete():
    os.system("python delete.py")

def searchrec():
    os.system("python searchrec.py")

def addrec():
    os.system("python addrecord.py")

def mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

def onscroll(axis, *args):
    global canvas
    if axis == 'y-axis':
        canvas.yview(*args)
    else:
        assert False, f"axis {axis} is incorrect, use 'x-axis' or 'y-axis'"
def showall():
    global canvas
    win1=Tk()
    win1.title("Display record")
    win1.geometry("360x340")
    win1.config(bg="black")
    win1.resizable(0,0)
    win1.iconbitmap("lite.ico")
    frame=Frame(win1)
    frame.pack()
    yscrollbar = Scrollbar(frame, orient='vertical',command=lambda *args: onscroll('y-axis', *args))
    
    yscrollbar.pack(side="right",anchor="w",fill="both")
    canvas=Canvas(frame,bg="black",width="350",height="300",scrollregion=(0, 0, 0, 2050),yscrollcommand=yscrollbar.set)
    canvas.pack()
    main_frame=Frame(canvas,bg="black")
    canvas.create_window((0,0),window=main_frame,anchor="nw")
    canvas.yview_scroll(100, "units")
    canvas.xview_scroll(100, "units")
    Label(main_frame,text="U.No.",bg="black",fg="white",font=("Georgia",12)).grid(row=0,column=0)
    Label(main_frame,text="Name",bg="black",fg="white",font=("Georgia",12)).grid(row=0,column=1,padx=30)
    Label(main_frame,text="Class",bg="black",fg="white",font=("Georgia",12)).grid(row=0,column=2,padx=30)
    Label(main_frame,text="Hg No.",bg="black",fg="white",font=("Georgia",12)).grid(row=0,column=3)
    with open("main.csv") as file:
        read=csv.reader(file)
        count=0
        row_value=1
        for i in read:
            Label(main_frame,text=i[0],bg="black",fg="white",font=("Georgia",12)).grid(row=row_value,column=0)
            Label(main_frame,text=i[1],bg="black",fg="white",font=("Georgia",12)).grid(row=row_value,column=1)
            Label(main_frame,text=i[2],bg="black",fg="white",font=("Georgia",12)).grid(row=row_value,column=2)
            Label(main_frame,text=i[3],bg="black",fg="white",font=("Georgia",12)).grid(row=row_value,column=3)
            row_value+=1
            count+=1
            win1.bind_all("<MouseWheel>",mousewheel)
    win1.mainloop()
win=Tk()

bg_icon=ImageTk.PhotoImage(file="Capture.jpg")
bg_lbl=Label(win,image=bg_icon).pack()

win.title(" Student Database Management")

win.geometry("840x700+0+0")

win.config(bg="black")

win.resizable(0,0)

win.iconbitmap("lite.ico")

b1=Button(win,text="DISPLAY RECORDS",bg="white",fg="red",border=10,relief="raise",font=("algerian",15),width=31,command=showall)
b1.place(x=420,y=500)
b2=Button(win,text="Add Record",bg="white",fg="red",border=10,relief="raise",font=("algerian",15),width=31,command=addrec)
b2.place(x=22,y=435)
b3=Button(win,text="Search Records",bg="white",fg="red",border=10,relief="raise",font=("algerian",15),width=31,command=searchrec)
b3.place(x=420,y=435)
b4=Button(win,text="Edit Record",bg="white",fg="red",border=10,relief="raise",font=("algerian",15),width=31,command=edit)
b4.place(x=22,y=500)
b5=Button(win,text="Delete Record",bg="white",fg="red",border=10,relief="raise",font=("algerian",15),width=31,command=delete)
b5.place(x=420,y=562)
b6=Button(win,text="Quit",bg="white",fg="red",border=10,relief="raise",font=("algerian",15),width=31,command=close)
b6.place(x=22,y=563)

win.mainloop()

