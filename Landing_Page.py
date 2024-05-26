import sys
import tkinter as tk
from tkinter import PhotoImage,font
import json

name=sys.argv[1]
username=sys.argv[2]
password =sys.argv[3]

root = tk.Tk()
root.title("Landing Page")
root.geometry('430x610')

def only_num(char):
    return char.isdigit()

def button():
    import subprocess
    expense=""
    money = InputField.get()
    money=int(money)
    
    with open("data.json", "r") as f:
        data=json.load(f)
        
    if username in data:
        data[username]["graph"]["money"].append(money)
        if data[username]["graph"]["increments"]:
            last_increment = data[username]["graph"]["increments"][-1]
        else:
            last_increment = 0
        data[username]["graph"]["increments"].append(last_increment)

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    print(data[username])
    root.withdraw()
    subprocess.run(['python', 'main.py', name, username, password, str(money),expense])

bg_color = '#121420'
text_color = '#FFFAFF'
input_color = '#30BCED'
spctext_color = '#45CB85'
root.configure(bg=bg_color)

logo = tk.Frame(root, bg=bg_color)
logo.pack(fill='x')

photo = PhotoImage(file="Logo.png")
photo = photo.subsample(5, 5)
label_img = tk.Label(logo, image=photo, bg=bg_color)
label_img.image = photo  
label_img.pack(pady=(20, 0))


Heading = tk.Label(root, text=f'Hello {name}', bg=bg_color, fg=spctext_color, font=("Helvetica", 26))
Heading.pack(pady=(20, 10)) 

Intro = tk.Label(root, 
    text="Ever wonder where all your cash goes? BudgeBuddy makes it easy to keep track of your physical cash so you can budget better and spend wisely.",
    bg=bg_color, fg=text_color, font=("Helvetica", 12), wraplength=400, justify="center")
Intro.pack(pady=(20, 20)) 

act_text = tk.Label(root,
    text="Enter Your Current Cash Amount to Get Started!", bg=bg_color, fg=spctext_color, font=("Helvetica", 13),
    justify="center")
act_text.pack(pady=(20,0))

large_font = font.Font(family="Helvetica", size=15)
validcmd = (root.register(only_num), '%S')
InputField = tk.Entry(root, bg=text_color, fg=bg_color, justify="center", font=large_font, validate="key", validatecommand=validcmd)
InputField.pack(pady=(5, 10))

but = tk.Button(root, text="Lets Go!",command=button, bg=input_color, fg=text_color, width=9, height=2)
but.pack(pady=(15,30))

Concl= tk.Label(root,
    text="Your privacy and security are our top priority. All data is encrypted with industry-standard security protocols.",
    bg=bg_color, fg=text_color, justify="center", font=("Helvetica", 12), wraplength=400)
Concl.pack(pady=(5,0))
root.mainloop()
