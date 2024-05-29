import tkinter as tk
from tkinter import PhotoImage
import subprocess
import json
expense="0"


#   This function is activated when Login button is clicked on the form.
def login_action():
    # This reads data from the JSON file and then can change value from it
    with open("data.json", "r") as f:
        data=json.load(f)
    # It takes up username of the user
    username = entry_username.get()
    # It takes up password of the user 
    password = entry_password.get()
    # It takes up name of the user
    name = entry_name.get()
  # It check if the username exists and the password matches
    if username in data and data[username]['password'] == password:
        # Check if the name matches
        if 'name' in data[username] and data[username]['name'] == name:
            print("Welcome back, {}!".format(name))
            print(data[username])
            money_list=data[username]["graph"]["money"]
            money=str(money_list[-1])
            # It stops the app from running
            app.withdraw()
            # It runs main.py when the username, password nad name is correct and present in JSON file
            subprocess.run(['python', 'main.py', name, username, password, money, expense])
        else:
            print("Name does not match. Please try again.")
    else:
        print("Invalid login credentials. Please try again.")

# This button when clicked shows/hides Password of the user
def toggle_password():
    if entry_password.cget('show') == '':
        entry_password.config(show='*')
        btn_toggle.config(text='See Password')
    else:
        entry_password.config(show='')
        btn_toggle.config(text='Hide Password')

# This button takes the user to the signup page of website
def open_signup():
    app.withdraw()
    subprocess.run(['python', 'Signup.py'])

app = tk.Tk()
app.title("Budgebuddy Login")
app.geometry("430x610")

# Colors used in app
background_color = "#E6F9E6"
box_color = "#66BB6A"
text_color = "#000000"
input_color = "#FFFFFF"

app.configure(bg=background_color)

# It is the frame of logo
logo_frame = tk.Frame(app, bg=background_color)
logo_frame.place(relwidth=1, height=200, relx=0, rely=0)

# It is the logo situated at the top
photo_image = PhotoImage(file="Logo.png")
photo_image = photo_image.subsample(5, 5)
label_image = tk.Label(logo_frame, image=photo_image, bg=background_color)
label_image.image = photo_image
label_image.pack(pady=(20, 0))

# It is the text of Login Form
label_login = tk.Label(app, text="Login Form", bg=background_color, fg=text_color, font=(24))
label_login.place(relx=0.4, rely=0.25)

# It is the frame of login form
login_frame = tk.Frame(app, borderwidth=2, relief='solid', bg=box_color)
login_frame.place(relwidth=0.9, relheight=0.5, relx=0.05, rely=0.3)

# It is the input field of Name
label_name = tk.Label(login_frame, text="Name", bg=box_color, fg=text_color)
label_name.pack(pady=(10, 5))
entry_name = tk.Entry(login_frame, bg=input_color, fg=text_color)
entry_name.pack(pady=(0, 5))

# It is the input field of Username
label_username = tk.Label(login_frame, text="Username", bg=box_color, fg=text_color)
label_username.pack(pady=(20, 5))
entry_username = tk.Entry(login_frame, bg=input_color, fg=text_color)
entry_username.pack(pady=(0, 20))

# It is the input field of Password
label_password = tk.Label(login_frame, text="Password", bg=box_color, fg=text_color)
label_password.pack(pady=(0, 5))
entry_password = tk.Entry(login_frame, show="*", bg=input_color, fg=text_color)
entry_password.pack(pady=(0, 5))
btn_toggle = tk.Button(login_frame, text="See Password", command=toggle_password, bg='#E0F5EA', fg=text_color)
btn_toggle.pack(pady=(5, 20))

# It is the Login button which redirects user to main page
button_login = tk.Button(login_frame, text="Login", command=login_action, bg=input_color, fg=text_color)
button_login.pack(pady=(0, 20))

# It is the button that takes user to the sign up page.
label_sign_up = tk.Label(app, text="Don't Have an Account, ", bg=background_color, fg=text_color)
label_sign_up.place(relx=0.2, rely=0.85)
btn_sign_up = tk.Button(app, text="Sign Up", command=open_signup, bg=background_color, fg="#4169E1", borderwidth=0)
btn_sign_up.place(relx=0.55, rely=0.85)

# This terminates the main loop
app.mainloop()
