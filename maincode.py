# welcome to my code
# please read comments i swear please please please
# This is a fork of David's inital code heavily modified by me
# By Paolo V
# UPDATE: fully compatable with windows operatin systems on python 3.13.0
# chromebook codespaces supported
# mac: No

import tkinter
import random # import the random library
import re # an important search/replace library

def main(): # we'll never revist this in the program lol
    encrypt_or_decrypt=input("d to decrypt, e to encry pt: ")
    if encrypt_or_decrypt == 'd':
        file_option=input("Input 'file' for txt file, or 'txt' for normaltext: ")
        decryptchoice(file_option)
    elif encrypt_or_decrypt == 'e':
        file_option=input("Input 'file' for txt file, or 'txt' for normal text: ")
        encryptchoice(file_option)
    else:
        print("Try again and write the right letter this time!")
        input("Press enter to continue...")
   
# checks user requested format for decryption, then asks for input
def decryptchoice(decryptformat): #i shall tell you
    if decryptformat == 'file': # hmmmm is the input file?
        txt_file_name=input("Please input your encrypted file, leave blank for default name (encrypted_file.txt): ") #ask to define txt_file_name
        if txt_file_name == '': # auto input!
            txt_file_name = 'encrypted_file.txt'# auto fill!
        decryptfile(txt_file_name) # go to decryptfile()
    elif decryptformat == 'txt':
        txtmsg=input("Please input your encrypted message: ") #msg must be manually inputed
        decrypt(txtmsg)
    else:
        print("Try again and write the right letter this time!")
        input("Press enter to continue...")

# checks user requested format for encryption, then asks for input
def encryptchoice(encryptformat): # same as decryptchoice()
    if encryptformat == 'file':
        txt_file_name=input("Please input your raw file: ")
        encryptfile(txt_file_name)
    elif encryptformat == 'txt':
        txtmsg=input("Please input your decrypted message: ")
        encrypt(txtmsg)
    else:
        print("Try again and write the right letter this time!")
        input("Press enter to continue...")

# encrypt for normal text
def encrypt(message):
    seed=random.randint(1,10**9) # look man look at encryptfile()
    random.seed(seed)
    for char in message: # look man im not gonna type comments for the same function i wrote in encrpytfile()
        msg_string=ord(char)
        msg_string=int(msg_string)
        msg_string=msg_string*random.randint(1,99)
        msg_string=msg_string*random.randint(1,99)
        print(msg_string, end=" ") # more simpler since its just a console msg
    print("\nSeed:", seed)
    input("Press enter to continue...") # so the user can see the output before the console closes

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

#decrypt normal message for normal text
def decrypt(message):
    seed=input("Please input the seed, it should have been a number printed after your message: ") # gotta ask the seed from user
    try: # key word TRY
        seed=int(seed) # suceed
    except ValueError: # fail lmao
        print("Invalid seed. Are you serious?") # punch the user "mentally"
        input("Press enter to continue...")
        return
    random.seed(seed) # gotta set the seed to the inputed seed from the encrypted message
    textlist=message.split() # split these god forsaken numbers so the program can read 
    numbers_list=[] # make a table
    for s in textlist:
        msg_string=int(s) # convert numbers to int
        msg_string=msg_string//random.randint(1,99) # divide by the same seed 
        msg_string=msg_string//random.randint(1,99) # again
        numbers_list.append(msg_string) # put that to the table
        result_string= "".join(chr(num) for num in numbers_list) # join the characters together for each string in the table
    print(result_string) # i finished please leave my family alone and my sleep schedule
    input("Press enter to continue...")

#decrypt function for file
def decryptfile(txtfile):
    try: 
        file=open(txtfile, "r") # man screw this i'm not gonna give you comments figure it out yourself
        seed=input("Please input the seed, it should have been a number in a file named encrypted_file_seed.txt after your message: ")
        try: # check if user is idiot
            seed=int(seed) # after that we go on
        except ValueError:
            print("Invalid seed. Are you serious?") # user is idiot
            input("Press enter to continue...")
            return
        random.seed(seed) # do something that i did in decrypt() i forgot
        num_string=file.read()  # tell the computer to read why
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
        print("output sent to decrypted_file.txt") # gotta tell the user
        input("Press enter to continue...")
    except FileNotFoundError: 
        print("File,", txtfile, "not found.") # user is stupid
        input("Press enter to continue...")

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