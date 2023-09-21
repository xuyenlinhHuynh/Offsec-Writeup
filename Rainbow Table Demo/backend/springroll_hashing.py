# Welcome to my very simple hashing function :)
# This is a self-made hashing algorithm using a random key added to each letter inside the password.
import random

# The hashing algorithm
def springroll_hashing(plaintext,key):
    # Only accept a key chosen from [1,50] inclusively
    if key < 1 or key > 50:
        warning = "Invalid input!!"
        return warning
    temp = []
    for letter in plaintext:
        # Add the key to each letter (make sure the letter has been converted into
        # integer) then append it to the temporary list
        temp.append(ord(letter)+key)
    # Join each element as hexadecimal in the list to the output (the prefix "0x" of the hex)
    output = "".join(hex(element) for element in temp).replace('0x','')
    return output

# Generating hashes for Task 1
# flag = open("one.txt", "r").read().split("\n")
# for line in flag:
#     fake_key = random.randint(1,50)
#     print(springroll_hashing(line,fake_key))

# Generating hashes for Task 2
# flag = open("pass.txt", "r").read().split("\n")
# for line in flag:
#     fake_key = random.randint(1,50)
#     print(springroll_hashing(line,fake_key))

# Generating hash for Task 3
# print(springroll_hashing("stR@ng",43))

# Generating hash for Task 4
# print(springroll_hashing("Jon@2k",29))