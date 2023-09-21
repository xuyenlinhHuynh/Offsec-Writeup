# This code is to generate the pre-computed hash table
from springroll_hashing import springroll_hashing

file = open("Rainbow Table Demo/springroll_hashing_table.txt", "a")
f = open("Rainbow Table Demo/backend/commonpass.txt", "r")

# Convert each line in the commonpass.txt file as an element in the list
s = list(f.read().split("\n"))
key = []

# Write down all po
for k in range(1,51):
    key.append(k)

for k in key:
    for line in s:
        file.write("key = "+str(k)+" --- "+line+": "+springroll_hashing(line,k)+"\n")

file.close()
f.close()