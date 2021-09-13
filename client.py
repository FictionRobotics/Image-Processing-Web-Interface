import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import socket
import time

x=3
host=""
port =5000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',port))

root=tk.Tk()
root.title("Fiction_Robotics")
root.iconbitmap(r'C:\Users\PC\Downloads\Logo.ico')
root['background']='dark blue'
root.geometry("600x400")

def close_window():
    root.destroy()

order_var=tk.StringVar()
user_var=tk.StringVar()
number_var=tk.StringVar()

def submit():
    global x
    global y
    password="ajgs"
    name=user_var.get()
    order=order_var.get()
    number=number_var.get()
    
    if number:
        x=x-int(number)
    else:
        messagebox.showerror("packages","please enter the valid packages")

    #print(x)
        
    
    print("The name is : " + name)
    print("The order is : " + order)
    print("the number of slots : " + number)

    if x>-1:
        y=x
        if (bool(name) and bool(order) and bool(number)):
            
            if name == 'A':
                package_num=number
                s.send(name.encode())
                time.sleep(1)
                s.send(order.encode())
                time.sleep(1)           
                s.send(number.encode())
                messagebox.showinfo("THANK YOU","Your Order is Placed")
            if name == 'B':
                package_num=number
                s.send(name.encode())
                time.sleep(1)
                s.send(order.encode())
                time.sleep(1)           
                s.send(number.encode())
                messagebox.showinfo("THANK YOU","Your Order is Placed")
            if name == 'C':
                package_num=number
                s.send(name.encode())
                time.sleep(1)
                s.send(order.encode())
                time.sleep(1)           
                s.send(number.encode())
                messagebox.showinfo("THANK YOU","Your Order is Placed")
    else:
        messagebox.showwarning("slots warning"," slots available :  " + str(y))

        if y>-1:
            x=y
    
            


        
    if not (name == 'A' or name == 'B' or name == 'C'):
        messagebox.showerror("username error",'Only user A,B and C are allowed!')
    if not (order == "Red"or order == "Blue"or order == "Green"):
        messagebox.showerror("order error","Please choose the package")
    if x < 1:
        messagebox.showwarning("slots warning","No more slots available")
        close_window()
    
    number=0


        
tk.Label(root, text = 'WELCOME TO CARGO DELIVERY SYSTEM',bg="dark blue",fg="white", font=('',10, 'bold')).grid(column = 1, row = 0, padx = 50, pady = 25)

tk.Label(root, text = "Username:",bg="dark blue",fg="white", font = ('calibre',10,'bold')).grid(column = 0, row = 5, padx = 10, pady = 25)
user=ttk.Combobox(root, width=27, textvariable=user_var)
user['values']=('A','B','C')
user.grid(column = 1, row = 5)


tk.Label(root, text = "Order package:",bg="dark blue",fg="white", font = ('calibre',10,'bold')).grid(column = 0, row = 10, padx = 10, pady = 25)
order=ttk.Combobox(root, width=27, textvariable=order_var)
order['values']=('Red','Blue','Green')
order.grid(column = 1, row = 10)

tk.Label(root, text = "number of slots:",bg="dark blue",fg="white", font = ('calibre',10,'bold')).grid(column = 0, row = 15, padx = 10, pady = 25)
number=ttk.Combobox(root, width=27, textvariable=number_var)
number['values']=('1','2','3')
number.grid(column = 1, row = 15)


sub_btn=tk.Button(root,bg='yellow',fg='black',text = 'Submit',font=('calibre',10,'bold'),command = submit)

sub_btn.grid(row=20,column=1)

root.mainloop()

