from tkinter import *
root = Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

root.title('Home')

Label().grid(row=0,column=0,padx=w//8)

bus_img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus_img).grid(row=0,column=1,columnspan=3)

Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='calibri 30 bold').grid(row=1,column=2)

def seatbooking():
    root.destroy()
    import Journey_details
Button(root,text='Seat Booking',bg='SpringGreen2',font='calibri 20 bold',command=seatbooking).grid(row=2,column=1,pady=h//30)

def checkbookings():
    root.destroy()
    import Check_bookings
Button(root,text='Check Booked Seat',bg='SpringGreen3',font='calibri 20 bold',command=checkbookings).grid(row=2,column=2)

def adddetails():
    root.destroy()
    import admin
Button(root,text='Add Bus Details',bg='SpringGreen4',font='calibri 20 bold',command=adddetails).grid(row=2,column=3)

Label(root,text='*For Admin only*',fg='red',font='Calibri 15 bold').grid(row=3,column=3)

root.mainloop()
