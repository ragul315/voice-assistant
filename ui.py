from customtkinter import *
from PIL import Image
import tkinter as tk
from speechreg import spreg

# Function to get the screen width and height
def get_screen_size():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    return screen_width, screen_height

# Function to calculate the position for bottom center
def calculate_bottom_center(width, height):
    screen_width, screen_height = get_screen_size()
    x = (screen_width - width) // 2
    y = screen_height - height-150
    return x, y

def button_click_callback(event):
    spreg()

app = CTk()
app.attributes("-topmost", True)  # Set the window to always stay on top
app.resizable(False, False) 

# Get the position for bottom center
x, y = calculate_bottom_center(200, 50)
app.geometry(f"200x50+{x}+{y}")  # Launch at bottom center
img = CTkImage(dark_image=Image.open("C:\\Users\\jragu\\Documents\\voice-assistant\\Src\\micw.png"),
               light_image=Image.open("C:\\Users\\jragu\\Documents\\voice-assistant\\Src\\micd.png"),
               size=(20,20))
btn = CTkButton(app, text="", image=img, corner_radius=100, width=15, height=40, fg_color="transparent")
btn.place(relx=0.5, rely=0.5, anchor="center")
btn.bind("<Button-1>", button_click_callback)
