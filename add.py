import sys
import tkinter as tk
from tkinter import PhotoImage,font
import subprocess
import json

counter_file="counter.txt"

def read_counter():
    try:
        with open(counter_file, "r") as f:
            count=int(f.read().strip())
        return count
    except FileNotFoundError:
        return 0

def write_counter(value):
    with open(counter_file, "w") as f:
        f.write(str(value))

x=read_counter()

name=sys.argv[1]
username= sys.argv[2]
password=sys.argv[3]
money= sys.argv[4]
ogmoney=int(money)

def only_num(char):
    return char.isdigit()

def hide_widget():
    widgets=[heading,cash_frame,entry_name,but,Pay_method,Date_time,Payee]
    for i in widgets:
        i.pack_forget()
    Payment_method.pack()
    Back.pack()
def show_widget():
    widgets=[heading,cash_frame,entry_name,but,Pay_method,Date_time,Payee]
    for i in widgets:
        i.pack()
    Payment_method.pack_forget()
    Back.pack_forget()

def button():
    global x
    x=int(x)
    x += 1
    x_str = str(x)
    expense = entry_name.get()
    expense = int(expense)
    newmoney = ogmoney - expense
    expense = str(expense)
    newexpense = "expense" + x_str
    money=newmoney
    with open("data.json", "r") as f:
        data=json.load(f)
    if username not in data:
        data[username] = {"name": name, "password": password, "money": newmoney}
    else:
        data[username]["graph"]["money"].append(newmoney)
    money=str(newmoney)
    data[username]["Counter"] = x
    data[username][newexpense] = expense
    data[username]["graph"]["increments"].append(x)
    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)
    del data["username"]
    write_counter(x)
    print(data[username])
    root.withdraw()
    subprocess.run(['python', 'main.py', name, username, password, money, expense])

root = tk.Tk()
root.title("Transactions")
root.geometry('430x610')

background_color = "#121420"
text_color1 = "#FFFAFF"
text_color2 = "#5EF38C"
box_color = "#303234"
extra = "#FFC857"
red_color = "#FF0000"

root.configure(bg=background_color)

Payment_method=tk.Frame(root, bg=background_color, width=610,height=430, bd=0, highlightthickness=0)
Back=tk.Button(Payment_method, bg=text_color2, fg=text_color1,command=show_widget, text="Back")

heading = tk.Label(root, text="Add Transaction", bg=background_color, fg=extra, font=("Helvetica", 20))
heading.pack(pady=(20,0),padx=(40,0))

cash_frame = tk.Frame(root, borderwidth=2, relief='solid', bg=box_color)
cash_frame.place(relwidth=1, relheight=0.25, relx=0.001, rely=0.15)

validcmd = (root.register(only_num), '%S')
entry_name = tk.Entry(cash_frame, width="9", bg=box_color, fg=red_color, font=("Helvetica", 60),validate="key", validatecommand=validcmd, justify="right", bd=0, highlightthickness=0)
entry_name.pack(pady=(30,0))

Pay_method=tk.Button(root, text="Payment Method",width=70, height=2,bg=box_color,fg=text_color1,font=("Helvetica", 12), command=hide_widget, justify="left",highlightthickness=1)
Pay_method.pack(pady=(250,0),padx=(0,0))

Date_time=tk.Button(root, text="Date and Time",width=70, height=2,bg=box_color,fg=text_color1,font=("Helvetica", 12), command=hide_widget, justify="left", highlightthickness=1)
Date_time.pack(pady=(0,0),padx=(0,0))

Payee=tk.Button(root, text="Payee",width=70, height=2,bg=box_color,fg=text_color1,font=("Helvetica", 12), command=hide_widget, justify="left", highlightthickness=1)
Payee.pack(pady=(0,0),padx=(0,0))

but = tk.Button(root, text="Done",command=button, bg=text_color2, fg=text_color1, width=9, height=2)
but.pack(pady=(50,0))





root.mainloop()
