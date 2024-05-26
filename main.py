import tkinter as tk
import sys
from tkinter import PhotoImage
import subprocess
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
    
name=sys.argv[1]
username=sys.argv[2]
password=sys.argv[3]
money=sys.argv[4]
expense1=sys.argv[5]

def green_btn(): 
    window.withdraw()
    subprocess.run(['python', 'add.py', name, username, password, money])

def print_user_data_on_logout():
    with open("data.json", "r") as f:
        data = json.load(f)
    print("User data on logout:", data.get(username, {}))

def logout_btn():
    print_user_data_on_logout()
    window.withdraw()
    subprocess.run(['python', 'Login.py'])


def draw_rounded_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    canvas.create_rectangle(x1 + radius, y1, x2 - radius, y1 + radius, **kwargs, outline="")
    canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, **kwargs, outline="")
    canvas.create_rectangle(x1 + radius, y2 - radius, x2 - radius, y2, **kwargs, outline="")
    canvas.create_oval(x1, y1, x1 + 2*radius, y1 + 2*radius, **kwargs, outline="")
    canvas.create_oval(x2 - 2*radius, y1, x2, y1 + 2*radius, **kwargs, outline="")
    canvas.create_oval(x1, y2 - 2*radius, x1 + 2*radius, y2, **kwargs, outline="")
    canvas.create_oval(x2 - 2*radius, y2 - 2*radius, x2, y2, **kwargs, outline="")

window = tk.Tk()
window.title('Main')
window.geometry('450x610')

background_color = "#121420"
text_color1 = "#FFFAFF"
text_color2 = "#5EF38C"
box_color = "#348AA7"
extra = "#FFC857"


window.configure(bg=background_color)

#Graph Color
color_background = "#d2f2d4"
color_axes_background = "#7be382"
color_plot_line = "#009c1a"
color_labels = "#22b600"
color_ticks = "#26cc00"

#Menu


menu_frame=tk.Canvas(window,height=700, width=40, bg=background_color, highlightthickness=0)
menu_frame.pack(padx=(0,0), pady=(20,0), side=tk.LEFT, anchor="nw")
menu_frame.pack_propagate(False)

draw_rounded_rectangle(menu_frame, 0, 0, 35, 550, 15, fill=box_color)

#Home Button
menu_photo = PhotoImage(file="home.png")
menu_photo = menu_photo.subsample(20, 20)
menu_home=tk.Button(menu_frame, image=menu_photo, bg=text_color1, bd=0, highlightthickness=0)
menu_home.place(x=3, y=30)

#Split Bill
bill_photo = PhotoImage(file="Bill.png")
bill_photo = bill_photo.subsample(4,4)
menu_bill=tk.Button(menu_frame, image= bill_photo, bg=box_color, bd=0, highlightthickness=0)
menu_bill.place(x=3, y=90)

#Logout
logout = PhotoImage(file="logout.png")
logout = logout.subsample(20,20)
logout_place=tk.Button(menu_frame, image= logout, bg=box_color, bd=0, highlightthickness=0, command=logout_btn)
logout_place.place(x=3, y=500)

# Cash 
income_frame = tk.Canvas(window, height=200, width=200, bg=background_color, highlightthickness=0)
income_frame.pack(padx=(5, 0), pady=(20, 20), side=tk.LEFT, anchor="nw")
income_frame.pack_propagate(False)

income_text = tk.Label(income_frame, text="Cash", bg=box_color, fg=text_color1, font=("Helvetica", 15), justify="left")
income_text.place(x=20, y=20)
        
income_value = tk.Label(income_frame, text=f"{money} INR", bg=box_color, fg=text_color2, font=("Helvetica", 20), justify="center", wraplength=140)
income_value.place(x=35, y=70)

def shrink_font_if_large_num():
    length= len(str(money))
    font_size=20
    if length > 9:
        font_size = 18
    income_value.config(font=("Helvetica", font_size))
shrink_font_if_large_num()

draw_rounded_rectangle(income_frame, 10, 10, 190, 150, 20, fill=box_color)

# Top Expenses

topex_frame = tk.Canvas(window, height=250, width=200, bg=background_color, highlightthickness=0)
topex_frame.pack(padx=(0,0), pady=(20,20),side=tk.LEFT, anchor="ne")
topex_frame.pack_propagate(False)

topex_text = tk.Label(topex_frame, text="Top Expenses", font=("Helvetica", 15),bg=box_color, fg=text_color1, justify="left")
topex_text.place(x=20,y=20)

with open("data.json", "r") as file:
    data = json.load(file)

user_data = data.get(username, {})


expenses = {k: int(v) for k, v in user_data.items() if k.startswith('expense')}
sorted_expenses = sorted(expenses.items(), key=lambda item: item[1], reverse=True)[:3]  # Get top 3 expenses

for idx, (exp_key, exp_value) in enumerate(sorted_expenses, start=1):
    exp_label = tk.Label(topex_frame, text=f"{idx}. {exp_value} INR", font=("Helvetica", 12), bg=box_color, fg=text_color2)
    exp_label.place(x=20, y=40 + idx*20)

draw_rounded_rectangle(topex_frame, 10, 10, 190, 150, 20, fill=box_color)


# Graph

with open("data.json","r") as f:
    data=json.load(f)

fig = Figure(figsize=(2.5,2.5), dpi=150, facecolor=box_color)  
ax = fig.add_subplot(111)
ax.set_facecolor(color_axes_background)

x_values = data[username]['graph']['increments']
y_values = data[username]['graph']['money']

ax.plot(x_values,y_values, marker="o", linestyle="-", color=color_plot_line)
ax.set_xlabel("Money", color=text_color1)
ax.set_ylabel("Expenses", color=text_color1)

fig.subplots_adjust(left=0.28, right=0.9, top=0.9, bottom=0.33)

Canvas = FigureCanvasTkAgg(fig, window)
Canvas.draw()
Canvas.get_tk_widget().place(x=55, y=180)

# Action button


green_button = tk.Canvas(window, height=150, width=400, bg=background_color, highlightthickness=0)
green_button.place(x=35, y=500)
action_text = tk.Button(green_button, text="+",font=("Helvetica", 23),bg=text_color2,cursor="hand1", fg=text_color1,highlightthickness=0,bd=0, justify="center", command=green_btn)
action_text.place(x=190, y=20)

draw_rounded_rectangle(green_button, 10, 10, 400, 75, 20, fill=text_color2)

window.mainloop()
