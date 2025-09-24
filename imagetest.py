import PIL
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox, Tk
import winsound
 # py -m pip install playsound
root = tk.Tk()
root.title("Encrypt / Decrypt Tool")
root.geometry("750x980")
x = r"rock.jpg"
tk.Button(root, text="play funny sound", width=20,
            command=lambda: winsound.PlaySound("bad-to-the-bone.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)).pack(pady=10)
im = Image.open(x)
im = ImageTk.PhotoImage(im)
label = tk.Label(root, image=im)
label.pack()

root.mainloop()
    

