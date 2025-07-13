import tkinter as tk
from tkinter.ttk import *
import presentation
import screenshort

def other():
 window = tk.Tk()
 window.title("OTHER")

 h1 = tk.Button(window, text='SCREENSHOT', fg='white', bg="orange",font=("calibre",35,"bold"),command=screenshort.sh)
 h1.place(x=35,y=70)


 h2 = tk.Button(window, text='PRESENTATION', fg='white', bg="orange",font=("calibre",32,"bold"),command=presentation.pr)
 h2.place(x=35,y=370)

 window.geometry("820x650")
 window.configure(bg="teal")
 window.mainloop()