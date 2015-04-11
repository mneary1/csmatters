'''
simple_caesar_cipher.py

Performs the encryption/decryption of messages using a Caesat Cipher.
Prompts the user to choose between Encryption/Decryption, then
to enter a message and a corresponding shift. 

The shift entered must have the same sign to encrypt and decrpyt the same message.

Author: Michael Neary <mneary1@umbc.edu>
Date: 04/11/2015
'''

'''
Performs the encryption of a message of using a Caesar Cipher. 
'''
def encrypt(message, shift):
	
	encrypted_message = ''

	#for each character in the message received
	for char in message:

		#encrypt the letter and add it to the encrypted message

		#checks if the character has ascii value of a lowercase letter
		if 97 <= ord(char) <= 122:

			#adding the shift might go over valid ascii for a lowercase letter
			#so shift by the number of letters up or down if needed
			if ord(char) + shift > 122:
				encrypted_message += chr(ord(char) + shift - 26)
			else:
				encrypted_message += chr(ord(char) + shift)

		#checks if the character has ascii value of an uppercase letter
		elif 65 <= ord(char) <= 90:

			#adding the shift might go over valid ascii for an uppercase letter
			#so shift by the number of letters up or down if needed
			if ord(char) + shift > 90:
				encrypted_message += chr(ord(char) + shift - 26)
			else:
				encrypted_message += chr(ord(char) + shift)

		#the character isn't a letter, so I choose not to encrypt it. 
		else:
			encrypted_message += char

	return encrypted_message

'''
Performs the decryption of a message of using a Caesar Cipher. 
'''
def decrpyt(message, shift):
	
	decrypted_message = ''

	#for each character in the message received
	for char in message:

		#decrypt the letter and add it to the decrypted message

		#checks if the character has ascii value of a lowercase letter
		if 97 <= ord(char) <= 122:

			#adding the shift might go over valid ascii for a lowercase letter
			#so shift by the number of letters up or down if needed
			if ord(char) - shift < 97:
				decrypted_message += chr(ord(char) - shift + 26)
			else:
				decrypted_message += chr(ord(char) - shift)

		#checks if the character has ascii value of an uppercase letter
		elif 65 <= ord(char) <= 90:

			#adding the shift might go over valid ascii for an uppercase letter
			#so shift by the number of letters up or down if needed
			if ord(char) - shift < 65:
				decrypted_message += chr(ord(char) - shift + 26)
			else:
				decrypted_message += chr(ord(char) - shift)

		#the character isn't a letter, so I choose not to encrypt it. 
		else:
			decrypted_message += char

	return decrypted_message

def main():

	print("Do you want to encrypt or decrpyt a message?")
	user_input = input("Enter e to encrypt, d to decrypt: ")

	message = input("Enter the message: ")
	shift = int(input("Enter the shift: "))
	
	if user_input == 'e':
		encrypted_message = encrypt(message, shift)
		print(encrypted_message)

	elif user_input == 'd':
		decrypted_message = decrpyt(message, shift)
		print(decrypted_message)

	else:
		print("I don't know what " + user_input + " means.")

main()
