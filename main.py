import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk
import MediaPlayer
import Mouse
import Shopping
import other

window = tk.Tk()
window.title("PCM ( PALM COMMUNICATION WITH MACHINE )")

#h1 = tk.Button(window, text=' P C M ', fg='black', width=10, bg="sky blue",font=("calibre",40,"bold"))
#h1.place(x=420,y=10)
h2 = tk.Label(window, text='|< P.C.M >|', fg='pink', width=10, bg="teal",font=("calibre",70,"bold"))
h2.place(x=180,y=15)

#PCM IMAGE
image = Image.open("C:\\Users\\ASUS\\OneDrive\\Desktop\\PROJECT\\HAND_GESTURE\\.vscode\\hand.png")
# Resize the image using resize() method
resize_image = image.resize((600, 900))
img = ImageTk.PhotoImage(resize_image)
# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.place(x=453,y=380)

#MEDIA PALYER
b1=tk.Button(window,text="MIDEA PLAYER" ,font=("Bahnschrift SemiBold SemiConden",25),bg="light yellow",fg="brown",command=MediaPlayer.media)
b1.place(x=10,y=600)
image = Image.open("C:\\Users\\ASUS\\OneDrive\\Desktop\\PROJECT\\HAND_GESTURE\\.vscode\\MEDIA.png")
# Resize the image using resize() method
resize_image = image.resize((350, 350))
img = ImageTk.PhotoImage(resize_image)
label1 = Label(image=img)
label1.image = img
label1.place(x=50,y=240)

#MOUSE
b2=tk.Button(window,text="  MOUSE  " ,font=("Bahnschrift SemiBold SemiConden",25),bg="light yellow",fg="brown" , width=13,command=Mouse.mouse)
b2.place(x=1070,y=600)
image = Image.open("C:\\Users\\ASUS\\OneDrive\\Desktop\\PROJECT\\HAND_GESTURE\\.vscode\\MOUSE.png")
# Resize the image using resize() method
resize_image = image.resize((350, 350))
img = ImageTk.PhotoImage(resize_image)
# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.place(x=1110,y=240)

#SHOPPING SITE
b3=tk.Button(window,text="SHOPPING SITE" ,font=("Bahnschrift SemiBold SemiConden",25),bg="light yellow",fg="brown",command=Shopping.shopping)
b3.place(x=10,y=1350)
image = Image.open("C:\\Users\\ASUS\\OneDrive\\Desktop\\PROJECT\\HAND_GESTURE\\.vscode\\shopping.png")
# Resize the image using resize() method
resize_image = image.resize((350, 350)) 
img = ImageTk.PhotoImage(resize_image)
# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.place(x=50,y=990)

#OTHERS
b4=tk.Button(window,text="OTHER" ,font=("Bahnschrift SemiBold SemiConden",25),bg="light yellow",fg="brown" ,width=13,command=other.other)
b4.place(x=1070,y=1350)
image = Image.open("C:\\Users\\ASUS\\OneDrive\\Desktop\\PROJECT\\HAND_GESTURE\\.vscode\\other.png")
 # Resize the image using resize() method
resize_image = image.resize((350, 350)) 
img = ImageTk.PhotoImage(resize_image)
# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.place(x=1110,y=990)

#window
window.geometry("1500x1500")
window.configure(bg="teal")
window.mainloop()


#SHOPPING SITE LINK
#https://www.flipkart.com/