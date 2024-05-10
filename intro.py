from tkinter import *
root = Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

bus_img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus_img).grid(row=0,column=0,padx=w/2.5)

Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='calibri 30 bold').grid(row=1,column=0)

Label(root,text='Name: Nimit Agarwal',fg='blue',font='calibri 21 bold').grid(row=2,column=0,pady=h//20)
Label(root,text='Er: 211B197',fg='blue',font='calibri 21 bold').grid(row=3,column=0)
Label(root,text='Mobile: 9520864362',fg='blue',font='calibri 21 bold').grid(row=4,column=0,pady=h//20)

Label(root,text='Submitted to: Dr. Mahesh Kumar',bg='light blue',fg='red',font='calibri 23 bold').grid(row=5,column=0)
Label(root,text='Project Based Learning',fg='red',font='calibri 18 bold').grid(row=6,column=0)

def destroy(e=1):
    root.destroy()
    import Home
root.bind('<KeyPress>',destroy)
root.mainloop()
