#importing hashlib module

import hashlib

#funcion for generationg md5 hash
def return_hash(text):
    hash=hashlib.md5(text.encode())
    return(hash.hexdigest())

#taking input text and printing hash


text = input("Enter Your Text: ")
print(f"Your md5 hash is {return_hash(text)}")
