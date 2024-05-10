from tkinter import *
root = Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

root.title('Add new details')

Label().grid(row=0,column=0,padx=w/6.5)

bus_img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus_img).grid(row=0,column=1,columnspan=7)

Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='calibri 24 bold').grid(row=1,column=1,columnspan=7,pady=h//90)
Label(root,text='Add New Details to DataBase',bg='sea green1',fg='Green',font='calibri 19 bold').grid(row=2,column=1,columnspan=7)

def  operator():
    root.destroy()
    import add_bus_operator_details
Button(root,text='New Operator',font='calibri 15 bold',bg='Pale green2',command=operator).grid(row=3,column=1,pady=h//80)

def bus():
    root.destroy()
    import add_bus_details
Button(root,text='New Bus',font='calibri 15 bold',bg='tomato',command=bus).grid(row=3,column=2,pady=25,padx=w//40)

def route():
    root.destroy()
    import add_route_details
Button(root,text='New Route',font='calibri 15 bold',bg='cornflower blue',command=route).grid(row=3,column=3,pady=h//80)

def run():
    root.destroy()
    import add_bus_running_details
Button(root,text='New Run',font='calibri 15 bold',bg='Salmon3',command=run).grid(row=3,column=4,pady=25,padx=w//40)

def home():
    root.destroy()
    import Home
home_img=PhotoImage(file='.\\home.png')
Button(root,image=home_img,bg='PaleGreen2',command=home).grid(row=4,column=1,columnspan=4)

root.mainloop()
