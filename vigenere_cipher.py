import string
import sys


class vigenere:

	def __init__(self):
		#a reference dictionery to get the reference for a correspoding alphabet
		self.str_upper = string.ascii_uppercase
		self.reference_dic = {}
		for i in range(26):
			self.reference_dic[self.str_upper[i]] = i


	#main encryption algorithm
	def encrypt(self, plain_text, key):
		#if text hash spaces and lowercases then replace it
		plain_text = plain_text.replace(" ","").upper()
		key = key.strip(" ").upper()
		deref = vigenere().dereference(plain_text)
		derefer_key = vigenere().dereference(key)
		row_cipher = []

		#adding plain text and key
		for i in range(len(deref)):	
			row_cipher.append((deref[i] + derefer_key[i % len(key)]) % 26 )

		#getting cipher from the list of cipher values
		cipher= ""
		for i in row_cipher:
			position = list(self.reference_dic.values()).index(i)
			char = list(self.reference_dic.keys())[position]
			cipher += char

		return cipher


	#decryption function
	def decrypt(self, cipher, key):
		cipher = cipher.strip(' ').upper()
		key = key.strip(' ').upper()
		deref = vigenere().dereference(cipher)
		derefer_key = vigenere().dereference(key)
		row_text = []

		#substructing cipher by the key
		for i in range(len(deref)):
			row_text.append((deref[i] - derefer_key[i % len(key)]) % 26 )

		#calculating real message from the list of number
		message = ""
		for i in row_text:
			position = list(self.reference_dic.values()).index(i)
			char = list(self.reference_dic.keys())[position]
			message += char

		return message



	#to get alphabet from the reference number
	def dereference(self, text):
		derefer_str = []
		for i in text:
			if i not in string.ascii_uppercase:
				print(f"you have entered an invalid value '{i}' for vigenere cipher")
				print("No SPACE, NUMBERS and SPECIAL CHARACTERs are ALLOWED @!!!!!!")
				sys.exit()
			derefer_str.append(self.reference_dic[i])

		return derefer_str



#calling functions and taking inputs
if __name__ == "__main__":
	while True:
		control = input("enter encrypt(e)/decrypt(d)/quit(q) : ")
		if control == "q" or control=="Q":
			break
		if control== "e" or control == "E":
			message = input("enter your message : ")
			message = message.strip(" ")
			key = input("enter your key : ")
			cipher = vigenere().encrypt(message, key)
			print(f"{cipher}\n")
		if control == "d" or control == "D":
			cipher = input("enter the cipher : ")
			key = input("enter the key : ")
			message = vigenere().decrypt(cipher, key)
			print(f"{message}\n")


