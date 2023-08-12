import random
chars = f"abcdefghijklmnopqrstuvwyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&()/?"
length = int(input("Enter Length: ") )
password=""
for a in range(length):
    password+=random. choice(chars)
print (password)
