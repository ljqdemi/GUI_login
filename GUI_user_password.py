import tkinter as tk
from tkinter import messagebox
 
def login_validation():
    username = entry_username.get()
    password = entry_password.get()
 
    if username == "admin" and password == "password123":
        messagebox.showinfo("登录成功", "登陆成功!")
    else:
        messagebox.showerror("登录失败", "用户名或密码有误!")
 
def create_ui():
    global entry_username
    global entry_password
 
    root = tk.Tk()
 
    root.title('用户登录页面')

    root.geometry('300x150')
 
    label_username = tk.Label(root, text="用户名:").place(x=50, y=30)
   

    entry_username = tk.Entry(root)
    entry_username.place(x=100, y=30)

 
    label_password = tk.Label(root, text="密码:").place(x=50, y=70)
    
 
    entry_password = tk.Entry(root, show="*")
    entry_password.place(x=100, y=70)
    
 
    button_login = tk.Button(root, text="登录", command=login_validation).place(x=100, y=110)
    
 
    root.mainloop()
 
create_ui()