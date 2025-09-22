import random
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox





def encrypt(msg):
    """Encrypt message by seeding RNG, then multiplying each char code by two random ints.
    Returns the space-separated numeric ciphertext and the seed used."""
    seed = random.randint(1, 10**9)
    random.seed(seed)
    parts = []
    for char in msg:
        val = ord(char)
        val = val * random.randint(1, 99)
        val = val * random.randint(1, 99)
        parts.append(str(val))
    encrypted = " ".join(parts)
    return encrypted, seed

def decrypt(encrypted_msg, seed):
    """Decrypt space-separated numeric ciphertext using the provided seed.
    Returns the plaintext or raises ValueError on invalid input."""
    try:
        seed = int(seed)
    except (TypeError, ValueError):
        raise ValueError("Invalid seed")

    random.seed(seed)
    textlist = encrypted_msg.split()
    numbers_list = []
    for s in textlist:
        n = int(s)
        n = n // random.randint(1, 99)
        n = n // random.randint(1, 99)
        numbers_list.append(n)
    try:
        result_string = "".join(chr(num) for num in numbers_list)
    except Exception as e:
        raise ValueError("Decryption produced invalid character codes") from e
    return result_string

window = tk.Tk()
window.title('Encryption/Decryption Tool')
window.geometry('1280x960')

def ask_and_encrypt():
    msg = simpledialog.askstring("Encrypt", "Enter the message to encrypt:")
    if not msg:
        return
    encrypted_msg, seed = encrypt(msg)
    # copy seed to clipboard
    window.clipboard_clear()
    window.clipboard_append(str(seed))
    window.update()  # ensure clipboard is updated on Windows
    # show encrypted data and note that seed was copied
    messagebox.showinfo(
        "Encrypted",
        f"Encrypted (space-separated numbers):\n{encrypted_msg}\n\nSeed:\n{seed}\n\n(The seed has been copied to the clipboard.)"
    )

def ask_and_decrypt():
    encrypted_msg = simpledialog.askstring("Decrypt", "Enter the encrypted message (space-separated numbers):")
    if not encrypted_msg:
        return
    seed = simpledialog.askinteger("Seed", "Enter the seed (the number shown after encryption):")
    if seed is None:
        return
    try:
        decrypted = decrypt(encrypted_msg, seed)
        messagebox.showinfo("Decrypted", decrypted)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

button_encrypt = ttk.Button(
    master=window,
    text="encrypt",
    command=ask_and_encrypt
)
button_encrypt.pack(pady=10)

button_decrypt = ttk.Button(
    master=window,
    text="decrypt",
    command=ask_and_decrypt
)
button_decrypt.pack(pady=10)

window.mainloop()
