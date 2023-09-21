import random
from textwrap import wrap

def decryption(hash):
    key = []
    for k in range(1,51):
        key.append(k)

    passwds = []
    for k in key:
        temp = "".join(chr(int(element, 16)-k) for element in wrap(hash, 2))
        passwds.append(temp)
    return passwds


output = "\n".join(decryption("9e9f7d6b9992"))
print(output)