import string
import sys


class vigenere:

	def __init__(self):
		#a reference dictionery to get the reference for a correspoding alphabet
		self.uppercase_ref = {}
		self.lowercase_ref = {}
		for index, char in enumerate(string.ascii_uppercase):
			self.uppercase_ref[char] = index
		for index, char in enumerate(string.ascii_lowercase):
			self.lowercase_ref[char] = index


	#main encryption algorithm
	def encrypt(self, plain_text, key):
		#formating and striping texts and keys
		plain_text = plain_text.strip()
		key = key.strip().lower()
		cipher = ""
		
		#adding plain text and key
		key_index = 0
		for p in plain_text:
			if p.islower():	
				cipher+= string.ascii_lowercase[(self.lowercase_ref[p] + self.lowercase_ref[ key[key_index % len(key)] ]) % 26 ]
				key_index+=1
			elif p.isupper():	
				cipher+= string.ascii_uppercase[(self.uppercase_ref[p] + self.lowercase_ref[ key[key_index % len(key)] ]) % 26 ]
				key_index+=1
			else:
				cipher += p

		return cipher


	#decryption function
	def decrypt(self, cipher, key):
		message = ""
		cipher = cipher.strip()
		key = key.strip().lower()
		if not key.isalpha():
			print("only letters are allowed in the key")
			print("exiting...")
			sys.exit()
		key_len = len(key)

		#substructing cipher by the key
		key_index = 0
		for i,c in enumerate(cipher):
			if c.islower():
				message+= string.ascii_lowercase[(self.lowercase_ref[c] - self.lowercase_ref[key[ key_index%key_len ]]) % 26 ]
				key_index+=1
			elif c.isupper():
				message+= string.ascii_uppercase[(self.uppercase_ref[c] - self.lowercase_ref[key[ key_index%key_len ]]) % 26 ]
				key_index+=1
			else:
				message+= c

		return message




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
			obj = vigenere()
			cipher = obj.encrypt(message, key)
			print(f"\n{cipher}\n\n")
		if control == "d" or control == "D":
			cipher = input("enter the cipher : ")
			key = input("enter the key : ")
			obj = vigenere()
			message = obj.decrypt(cipher, key)
			print(f"\n{message}\n\n")


