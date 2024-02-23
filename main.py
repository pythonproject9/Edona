import base64
import string


def e_b64(s): 
    """encode the string in base64"""
    return base64.b64encode(s.encode()).decode()


def d_b64(s): 
    """decode from encoded base64"""
    return base64.b64decode(s).decode()


def split_string(data, number):
    """Split the string in 'n' number of parts. and return a list"""

    hoo = []

    for i in range(len(number)):
        m = i+1
        n = len(data)//len(number)
        k = n * m
        if i == 0:
            hoo.append(data[:n])
        elif i == len(number)-1:
            hoo.append(data[n*i:])
        else:
            hoo.append(data[n*i:k])

    return hoo


def split_encode(splited_string, number, user_choice):
    """take the splited string and exceed the character index by give pin value."""

    # user_choice = int(input("Type:\n (1) to save password.\n (2) to decrypt password.\n >>> "))
    letters = list(string.printable)
    new_encoded_data = ""

    for i in range(len(number)):
        for ch in splited_string[i]:
            if ch in letters:
                index = letters.index(ch)
                pin_index = int(number[i])
                # here you can use decoding function through if-else statement.
                # new_encoded_data += letters[index+pin_index]
                if user_choice == 1:
                    new_encoded_data += letters[index+pin_index]
                elif user_choice == 2:
                    new_encoded_data += letters[index-pin_index]
                else:
                    break

    return new_encoded_data              



pin = input("\n[+] Enter your pin: ")
user_choice = int(input("\n[*] Type:-\n '1' to encrypt a password.\n '2' to decrypt a password.\n >>> "))


# through direct input
if user_choice == 1 and len(pin) < 5:
    data = input("\n[+] Enter your password: ")
    encoded_data = e_b64(data)
    split_data = split_string(encoded_data, pin)
    encrypted  = split_encode(split_data, pin, user_choice)
    print("\n[*] Encrypted password:", encrypted)
        
elif user_choice == 2 and len(pin) < 5:
    data = input("\n[+] Enter your encrypted password: ")
    split_encrypted = split_string(data, pin)
    split_decrypt = split_encode(split_encrypted, pin, user_choice)
    decoded_data = d_b64(split_decrypt)
    print("\n[*] Decrypted password:", decoded_data)
    print("\n")

else:
    print("[*] please choose a valid option and your pin should be less than 5 numbers.\n")  


# # through file
# if user_choice == 1 and len(pin) < 4:
#     with open("real_pass.txt", "r") as reading:
#         for paa in reading:
#             data = paa.strip()
#             encoded_data = e_b64(data)
#             split_data = split_string(encoded_data, pin)
#             encrypted  = split_encode(split_data, pin, user_choice)
#             with open("enc_pass.txt", "a") as saving:
#                 saving.write(f"{encrypted}\n")
        
# elif user_choice == 2 and len(pin) < 4:
#     with open("enc_pass.txt", "r") as reading:
#         for paa in reading:
#             enc = paa.strip()
#             split_encrypted = split_string(enc, pin)
#             split_decrypt = split_encode(split_encrypted, pin, user_choice)
#             decoded_data = d_b64(split_decrypt)
#             print("decrypted:", decoded_data)
# else:
#     print("[*] please choose a valid option and your pin should be less than 5 numbers")   


