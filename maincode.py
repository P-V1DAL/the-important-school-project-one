# welcome to my code
# please read comments i swear please please please
# This is a fork of David's inital code heavily modified by me
# By Paolo V
# UPDATE: fully compatable with windows operatin systems on python 3.13.0
# chromebook codespaces supported
# mac: No

import tkinter as tk
import random # import the random library
import re # an important search/replace library
from tkinter import filedialog, simpledialog, messagebox

def main():
    root = tk.Tk()
    root.title("Encrypt / Decrypt Tool")
    root.geometry("500x400")
    show_main_menu(root)
    root.mainloop()

def clear(root):
    for widget in root.winfo_children():
        widget.destroy()

def show_main_menu(root):
    clear(root)
    tk.Label(root, text="Do you want to encrypt or decrypt?", font=("Arial", 14)).pack(pady=20)

    tk.Button(root, text="Encrypt File", width=20,
              command=lambda: encryptchoice("file")).pack(pady=10)
    tk.Button(root, text="Decrypt File", width=20,
              command=lambda: decryptchoice("file")).pack(pady=10)

def encryptchoice(_fmt="file"):
    # pick input file, then run encryptfile
    filename = filedialog.askopenfilename(
        title="Select raw text file to encrypt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if not filename:
        messagebox.showinfo("Canceled", "No file selected.")
        return
    try:
        encryptfile(filename)
        messagebox.showinfo("Done", "Output written to encrypted_file.txt (seed included at end).")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decryptchoice(_fmt="file"):
    # pick encrypted file, ask for seed, then run decryptfile
    filename = filedialog.askopenfilename(
        title="Select encrypted file",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if not filename:
        messagebox.showinfo("Canceled", "No file selected.")
        return
    seed_str = simpledialog.askstring("Seed required", "Enter seed number printed at the end of the file:")
    if seed_str is None:
        messagebox.showinfo("Canceled", "No seed entered.")
        return
    try:
        seed = int(seed_str)
    except ValueError:
        messagebox.showerror("Error", "Invalid seed. It must be an integer.")
        return
    try:
        decryptfile(filename, seed)
        messagebox.showinfo("Done", "Output written to decrypted_file.txt")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# encrypt function for file
def encryptfile(txtfile):
    seed=random.randint(1,10**9) # a very critical part in encryption, get a random seed
    # seed=472230563 you can remove the comment to force a seed, this may be a user option in the future?
    random.seed(seed) # oops we gotta save the seed or else msg is bricked
    try: # the funny error catch to solve everyone's lives
        file=open(txtfile, "r") # put in read mode
        message=file.read() # then read the whole text in the function
        for char in message:
            msg_string=ord(char) # convert the character to the ascii value
            msg_string=int(msg_string) # just gotta convert it to int
            msg_string=msg_string*random.randint(1,99) # multiply with the random seed 
            msg_string=msg_string*random.randint(1,99) # multiply again with the same random seed
            with open('encrypted_file.txt', 'a') as f: # open the file in append mode (add-on mode)
                print(msg_string, end=' ', file=f) # printing the string in a sequence of numbers (adds a space too)
        with open('encrypted_file.txt', 'a') as f:
            print("\nSeed:", seed, file=f) # gotta print the seed or else bricked message oops :(
        print("output sent to encrypted_file.txt") # gotta tell the user
        input("Press enter to continue...")
    except FileNotFoundError: # finally a catch error
        print("File,", txtfile, "not found.") # nope, nope, nope, go back user, you suck at this
        input("Press enter to continue...")

#decrypt function for file
def decryptfile(txtfile, seed):
    file=open(txtfile, "r") # man screw this i'm not gonna give you comments figure it out yourself
    try: # check if user is idiot
        seed=int(seed) # after that we go on
    except ValueError:
        print("Invalid seed. Are you serious?") # user is idiot
        input("Press enter to continue...")
        return
    random.seed(seed) # do something that i did in decrypt() i forgot
    with open(txtfile, "r", encoding="utf-8", errors="replace") as file:
        num_string = file.read()
    num_string = re.sub(r"Seed:\s*\d+", "", num_string) # meant to remove (Seed:#seed) from the txt file
    msg_string=num_string.split() # split the numbers 
    word_list=[] # empty ahh table
    for s in msg_string:
        msg_string=int(s) 
        msg_string=msg_string//random.randint(1,99) #revse the encryption
        msg_string=msg_string//random.randint(1,99) 
        word_list.append(msg_string)
    with open('decrypted_file.txt', 'a') as f:
        result_string= "".join(chr(word) for word in word_list)
        print(result_string, file=f)

main()
# if you dont understand email me at paolov717@gmail.com
# or my school handle 705828@students.mcallenisd.net
# no im not putting my phone number
# look at the comments damn maybe get an ai to read it for you
# can i please get sleep
# i want to thank david for making the base
# Made in VS Code on a personal PC
# screw hb1481
# these chromebooks suck so bad and error out every 5 minutes
# i recommend you go download vs code on your personal laptop for cs at this point you're welcome
# omg i still have to do those slides
# HELP

# secret wip features i never got to add
# user defined seed
# user defined output file name 
# GUI: no
# image files: no
# better error handling: maybe (no)
# "All of this just works" todd howard at some at the fallout 4 showcase
# Hey guys its your friendly neighborhood dude that tried to do shit but couldnt do it because I suck at this shit lol. - Pepe
# we need to add a ui with tkinter