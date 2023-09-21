import random
from textwrap import wrap

def decryption(hash):
    key = []
    for k in range(1,51):
        key.append(k)

    for k in key:
        temp = "".join(chr(int(element, 16)-k) for element in wrap(hash, 2))
        if temp.startswith("Jon"):
            return [temp, k]
    return ["password not found", "key not found"]



output = decryption("678c8b5d4f88")
print("The password is: ",output[0])
print("The key is: ", output[1])