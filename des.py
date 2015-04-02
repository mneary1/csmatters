'''
encryption/decryption using DES
written by Michael Neary <mneary1@umbc.edu>
'''

import sys,os
from Crypto.Cipher import DES

def encrypt():
    key = input("Enter the 8-byte key to use: ")
    print("In practice, this key would be randomly generated. For now, entering it is fine.")
    print("Make sure you remember the key!")
    key = bytes(key)

    message = input("Enter the message you want to encrypt: ") 
    
    cipher = DES.new(key, DES.MODE_ECB)
    message = cipher.encrypt(message)
    print(message)

def decrypt():
    key = input("Enter the 8-byte key:")
    

def main():
    encrypt()
    
main()

