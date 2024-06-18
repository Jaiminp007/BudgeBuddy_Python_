import tkinter as tk
from tkinter import PhotoImage
import subprocess
import json

counter_file = "counter.txt"

def write_counter(value):
    with open(counter_file, "w") as f:
        f.write(str(value))

def signup_action():
    with open("data.json", "r") as f:
        data=json.load(f)
    
    username = entry_username.get()
    password = entry_password.get()
    password_again = entry_password_again.get()
    name = entry_name.get()
    x="0"

    if password!=password_again:
        print("Error write again")
        app.withdraw()
        subprocess.run(['python', 'Signup.py'])
    
    else:
        if username not in data:
            data[username] = {
            "name": name,
            "password": password,
            "graph": {
                "increments": [],
                "money": []
            }
        }
        else:
            print("Username already exists.")
            return
        
        data[username]["Counter"] = x
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
        print(data[username])
        write_counter(x)
        app.withdraw()
        subprocess.run(['python', 'Landing_Page.py', name, username, password])

def toggle_password():
    if entry_password.cget('show') == '':
        entry_password.config(show='*')
        btn_toggle.config(text='See Password')
    else:
        entry_password.config(show='')
        btn_toggle.config(text='Hide Password')

def toggle_password_again():
    if entry_password_again.cget('show') == '':
        entry_password_again.config(show='*')
        btn_toggle_again.config(text='See Password')
    else:
        entry_password_again.config(show='')
        btn_toggle_again.config(text='Hide Password')

def open_login():
    app.withdraw()
    subprocess.run(['python', 'Login.py'])

app = tk.Tk()
app.title("Budgebuddy Login")
app.geometry("430x610")

background_color = "#E6F9E6"
box_color = "#66BB6A"
text_color = "#000000"
input_color = "#FFFFFF"

app.configure(bg=background_color)

logo_frame = tk.Frame(app, bg=background_color)
logo_frame.place(relwidth=1, height=200, relx=0, rely=0)

photo_image = PhotoImage(file="Logo.png")
photo_image = photo_image.subsample(5, 5)
label_image = tk.Label(logo_frame, image=photo_image, bg=background_color)
label_image.image = photo_image
label_image.pack(pady=(20, 0))

label_login = tk.Label(app, text="Sign Up Form", bg=background_color, fg=text_color, font=(24))
label_login.place(relx=0.4, rely=0.25)

login_frame = tk.Frame(app, borderwidth=2, relief='solid', bg=box_color)
login_frame.place(relwidth=0.9, relheight=0.5, relx=0.05, rely=0.3)

label_name = tk.Label(login_frame, text="Name", bg=box_color, fg=text_color)
label_name.pack(pady=(10, 5))
entry_name = tk.Entry(login_frame, bg=input_color, fg=text_color)
entry_name.pack(pady=(0, 5))

label_username = tk.Label(login_frame, text="Username", bg=box_color, fg=text_color)
label_username.pack(pady=(0, 5))
entry_username = tk.Entry(login_frame, bg=input_color, fg=text_color)
entry_username.pack(pady=(0, 5))

label_password = tk.Label(login_frame, text="Password", bg=box_color, fg=text_color)
label_password.pack(pady=(0, 5))
entry_password = tk.Entry(login_frame, show="*", bg=input_color, fg=text_color)
entry_password.pack(pady=(0, 5))
btn_toggle = tk.Button(login_frame, text="See Password", command=toggle_password, bg='#E0F5EA', fg=text_color)
btn_toggle.place(x=280,y=130)

label_password_again = tk.Label(login_frame, text="Re-enter Password", bg=box_color, fg=text_color)
label_password_again.pack(pady=(0, 5))
entry_password_again = tk.Entry(login_frame, show="*", bg=input_color, fg=text_color)
entry_password_again.pack(pady=(0, 5))
btn_toggle_again = tk.Button(login_frame, text="See Password", command=toggle_password_again, bg='#E0F5EA', fg=text_color)
btn_toggle_again.place(x=280,y=180)

button_signup = tk.Button(login_frame, text="Signup", command=signup_action, bg=input_color, fg=text_color)
button_signup.pack(pady=(30, 20))

label_login = tk.Label(app, text="Have an Account, ", bg=background_color, fg=text_color)
label_login.place(relx=0.2, rely=0.85)
btn_login = tk.Button(app, text="Login", command=open_login, bg=background_color, fg="#4169E1", borderwidth=0)
btn_login.place(relx=0.55, rely=0.85)

app.mainloop()
