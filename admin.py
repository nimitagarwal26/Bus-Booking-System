from tkinter import *
from tkinter.messagebox import *
import sqlite3
root = Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
bus_img=PhotoImage(file='.\\Bus_for_project.png')
Label().grid(row=0,column=0,padx=380)
Label(root,image=bus_img).grid(row=0,column=1,columnspan=4)
Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='calibri 28 bold').grid(row=1,column=1,columnspan=4)


frame=Frame(root,relief='groove',bd=5)

frame.grid(row=2,column=2,pady=h//60)
Label(frame,text="Enter Login Details",font='calibri 18 bold').grid(row=3,column=1,columnspan=4)
Label(frame,text="Username:",font='calibri 14').grid(row=4,column=1)
u_name=Entry(frame,width='20')
u_name.grid(row=4,column=2,padx=w//60)
Label(frame,text="Password:",font='calibri 14').grid(row=5,column=1,pady=h//90)
u_pass=Entry(frame,width='20',show='*')
u_pass.grid(row=5,column=2,padx=w//60)


def login():
    name=u_name.get()
    password=u_pass.get()
    if name=='':
        showerror('Error','Enter your Username')
    elif password=='':
        showerror('Error','Enter your Password')
    else:
        con=sqlite3.Connection('bus_reservation_211b197')
        cur=con.cursor()

        cur.execute('''select count(*) from admin where username=? and password=?''',(name,password))
        a=cur.fetchone()
        count=a[0]
        if count==1:
            root.destroy()
            import add_new_details
        else:
            showerror('Error','Wrong username or password')
        con.commit()
        con.close()
Button(root,text="Login",font='calibri 18 bold',bg='SpringGreen2',command=login).grid(row=6,column=1,columnspan=4,pady=h//70)
def home():
    root.destroy()
    import Home
home_img=PhotoImage(file='.\\home.png')
Button(root,image=home_img,bg='PaleGreen2',command=home).grid(row=7,column=1,columnspan=4)
