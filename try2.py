from tkinter import *
from tkinter.messagebox import *
root = Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

root.title('Add bus details')

Label().grid(row=0,column=0,padx=w//10)

bus_img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus_img).grid(row=0,column=1,columnspan=13)

Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='calibri 24 bold').grid(row=1,column=1,columnspan=13,pady=h//70)
Label(root,text='Add Bus Details',bg='sea green1',fg='Green',font='calibri 19 bold').grid(row=2,column=1,columnspan=13)

Label(root,text='Bus Id',font='calibri 15 bold').grid(row=3,column=1,pady=20,padx=w//100)
busid=Entry(root,width='10')
busid.grid(row=3,column=2)

Label(root,text='Bus Type',font='calibri 15 bold').grid(row=3,column=3,padx=w//100)
bus_type=StringVar()
types=('AC 2x2','AC 3x2','Non AC 2x2','Non AC 3x2','AC-Sleeper 2x1','Non-AC Sleeper 2x1')
bus_type.set('Bus type')
menu=OptionMenu(root,bus_type,*types)
menu.config(font='calibri 14 bold')
menu["menu"].config(bg='SteelBlue1',font='calibri 14')
menu.grid(row=3,column=4)

Label(root,text='Capacity',font='calibri 15 bold').grid(row=3,column=5,pady=20,padx=w//100)
capacity=Entry(root,width='7')
capacity.grid(row=3,column=6)

Label(root,text='Fare Rs',font='calibri 15 bold').grid(row=3,column=7,pady=20,padx=w//100)
fare=Entry(root,width='8')
fare.grid(row=3,column=8)

Label(root,text='Operator Id',font='calibri 15 bold').grid(row=3,column=9,pady=20,padx=w//100)
oid=Entry(root,width='10')
oid.grid(row=3,column=10)

Label(root,text='Route Id',font='calibri 15 bold').grid(row=3,column=11,pady=20,padx=w//100)
rid=Entry(root,width='8')
rid.grid(row=3,column=12)

def check_details():
    if busid.get()=='':
        showerror('Error','Please enter Bus Id')
    elif bus_type.get()=='Bus type':
        showerror('Error','Please select Bus Type')
    elif capacity.get()=='':
        showerror('Error','Please enter Capacity')
    elif fare.get()=='':
        showerror('Error','Please enter Fare')
    elif oid.get()=='':
        showerror('Error','Please enter Operator Id')
    elif rid.get()=='':
        showerror('Error','Please enter Route Id')
    else:
        showinfo('Bus entry','Bus record added Successfully')
Button(root,text='Add Bus',font='calibri 14 bold',bg='PaleGreen2',command=check_details).grid(row=4,column=5,padx=w//100)


def edit_details():
    if busid.get()=='':
        showerror('Error','Please enter Bus Id')
    elif bus_type.get()=='Bus type':
        showerror('Error','Please select Bus Type')
    elif capacity.get()=='':
        showerror('Error','Please enter Capacity')
    elif fare.get()=='':
        showerror('Error','Please enter Fare')
    elif oid.get()=='':
        showerror('Error','Please enter Operator Id')
    elif rid.get()=='':
        showerror('Error','Please enter Route Id')
    else:
        showinfo('Bus updation','Bus record updated successfully')       
Button(root,text='Edit Bus',font='calibri 14 bold',bg='PaleGreen2',command=edit_details).grid(row=4,column=6)

def home():
    root.destroy()
    import Home
home_img=PhotoImage(file='.\\home.png')
Button(root,image=home_img,bg='PaleGreen2',command=home).grid(row=4,column=7,padx=w//100)

root.mainloop()
