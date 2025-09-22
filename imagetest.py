import PIL
from PIL import Image, ImageTk
import tkinter 
import winsound
from tkinter import filedialog, simpledialog, messagebox, Tk
root = tkinter.Tk()
root.title("Encrypt / Decrypt Tool")
root.geometry("750x980")
x = r"C:\Users\705828\Downloads\oip.png"
im = Image.open(x)
im = ImageTk.PhotoImage(im)
label = tkinter.Label(root, image=im)
label.pack()
tkinter.Button(root, text="Encrypt File", width=20,
            command=lambda: winsound.Beep(frequency=2000,duration=2000)).pack(pady=10)
root.mainloop()
    

