# Welcome to my very simple hashing function :)
import random

def springroll_hashing(plaintext,key):
    if key < 1 or key > 50:
        warning = "Invalid input!!"
        return warning
    temp = []
    for word in plaintext:
        temp.append(ord(word)+key)
    output = "".join(hex(element) for element in temp).replace('0x','')
    return output