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
Label(frame,text="Sign Up",font='calibri 18 bold').grid(row=3,column=1,columnspan=4)
Label(frame,text="First Name:",font='calibri 14').grid(row=4,column=1)
e_fname=Entry(frame,width='20')
e_fname.grid(row=4,column=2,padx=w//60)
Label(frame,text="Last Name:",font='calibri 14').grid(row=5,column=1,pady=h//90)
e_lname=Entry(frame,width='20')
e_lname.grid(row=5,column=2,padx=w//60)
Label(frame,text="Email:",font='calibri 14').grid(row=6,column=1,pady=h//90)
e_email=Entry(frame,width='20')
e_email.grid(row=6,column=2,padx=w//60)
Label(frame,text="Phone Number:",font='calibri 14').grid(row=7,column=1,pady=h//90)
e_phn=Entry(frame,width='20')
e_phn.grid(row=7,column=2,padx=w//60)
Label(frame,text="Create Username:",font='calibri 14').grid(row=8,column=1,pady=h//90)
e_uname=Entry(frame,width='20')
e_uname.grid(row=8,column=2,padx=w//60)
Label(frame,text="Create Password:",font='calibri 14').grid(row=9,column=1,pady=h//90)
e_cpass=Entry(frame,width='20',show='*')
e_cpass.grid(row=9,column=2,padx=w//60)
Label(frame,text="Re-enter Password:",font='calibri 14').grid(row=10,column=1,pady=h//90)
e_rpass=Entry(frame,width='20',show='*')
e_rpass.grid(row=10,column=2,padx=w//60)


def signup():
    fname=e_fname.get()
    lname=e_lname.get()
    email=e_email.get()
    phn=e_phn.get()
    uname=e_uname.get()
    cpass=e_cpass.get()
    rpass=e_rpass.get()
    
    if fname=='':
        showerror('Error','Enter your First name')
    elif lname=='':
        showerror('Error','Enter your Last name')
    elif email=='':
        showerror('Error','Enter your Email')
    elif phn=='':
        showerror('Error','Enter your Phone Number')
    elif uname=='':
        showerror('Error','Create your Username')
    elif cpass=='':
        showerror('Error','Create your Password')
    elif rpass=='':
        showerror('Error','Re-enter your Password')
    elif cpass!=rpass:
        showerror('Error',"Your password doesn't match")
    else:
        con=sqlite3.Connection('bus_reservation_211b197')
        cur=con.cursor()

        cur.execute('''insert into user_details(fname ,lname ,Email ,phone_number ,username ,password) values(?,?,?,?,?,?)''',(fname,lname,email,phn,uname,rpass))
        showinfo('Successful','Sign Up successful.\n You can book you seat now.')
        con.commit()
        con.close()
Button(root,text="Sign Up",font='calibri 18 bold',bg='SpringGreen2',command=signup).grid(row=11,column=1,columnspan=4,pady=h//70)
def home():
    root.destroy()
    import Home
home_img=PhotoImage(file='.\\home.png')
Button(root,image=home_img,bg='PaleGreen2',command=home).grid(row=14,column=1,columnspan=4)
