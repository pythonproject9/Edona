import base64
import string
from tkinter import *


def split_string(data, number):
    """Split the string in 'n' number of parts. and return a list"""

    parts = []

    for i in range(number):
        m = i+1
        n = len(data)//number  # each parts should have this number of characters.
        if i == 0: # It run for making first part.
            parts.append(data[:n])  # it is same as n
        elif i == number-1: # it runs for making last part.  
            parts.append(data[n*i:])
        else: # it runs for making middle parts.
            parts.append(data[n*i:n*m])

    return parts


def encryption(data, pin):
    """take the splited string and exceed the character index by given pin value respectively."""

    pin_len = len(pin)
    b64_encode = base64.b64encode(data.encode()).decode()
    splited_b64e_data = split_string(b64_encode, pin_len)
    letters = list(string.printable)
    new_encoded_data = ""

    for i in range(pin_len):
        for ch in splited_b64e_data[i]:
            if ch in letters:
                index = letters.index(ch)
                pin_index = int(pin[i])
                new_encoded_data += letters[index+pin_index]

    return new_encoded_data


def decryption(data, pin):
    """take the splited string and exceed the character index by given pin value respectively."""

    pin_len = len(pin)
    splited_b64e_data = split_string(data, pin_len)
    letters = list(string.printable)
    b64_encoded_data = ""

    for i in range(pin_len):
        for ch in splited_b64e_data[i]:
            if ch in letters:
                index = letters.index(ch)
                pin_index = int(pin[i])
                b64_encoded_data += letters[index-pin_index]

    b64_decoded_data = base64.b64decode(b64_encoded_data).decode()
    return b64_decoded_data


def clip(text):
    window.clipboard_clear()
    window.clipboard_append(text)

def enc():
    data = pass_entry.get()
    pin = pin_entry.get()
    encryted_data = encryption(data, pin)
    # clip_button.config(text=encryted_data)
    show_label.config(text=encryted_data)
    clip(encryted_data)

def dec():
    data = pass_entry.get()
    pin = pin_entry.get()
    decryted_data = decryption(data, pin)
    # clip_button.config(text=decryted_data)
    show_label.config(text=decryted_data)
    clip(decryted_data)



FONT = ("Arial", 15, "normal")


window = Tk()
window.title("Encrypt >< Decrypt")
window.config(padx=20, pady=20)

pin_label = Label(text="Pin:", font=FONT)
pin_label.grid(row=0, column=0)


pin_entry = Entry(width=20, font=FONT)
pin_entry.grid(row=0, column=2, pady=15)


pass_label = Label(text="Password:", font=FONT)
pass_label.grid(row=1, column=0)


pass_entry= Entry(width=20, font=FONT)
pass_entry.grid(row=1, column=2)


enc_button = Button(text="Encrypt", font=FONT, command=enc)
enc_button.grid(row=2, column=0, pady=15)


dec_button = Button(text="Decrypt", font=FONT, command=dec)
dec_button.grid(row=2, column=2, pady=50)


show_label = Label(text="", font=FONT)
show_label.grid(row=3, column=1)

window.mainloop()