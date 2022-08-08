import string


class vigenere:

	def __init__(self):
		self.str_upper = string.ascii_uppercase
		self.reference_dic = {}
		for i in range(26):
			self.reference_dic[self.str_upper[i]] = i


	def encrypt(self, plain_text, key):
		plain_text = plain_text.upper()
		key = key.upper()
		deref = vigenere().dereference(plain_text)
		derefer_key = vigenere().dereference(key)
		row_cipher = []

		for i in range(len(deref)):	
			row_cipher.append((deref[i] + derefer_key[i % len(key)]) % 26 )

		cipher= ""
		for i in row_cipher:
			position = list(self.reference_dic.values()).index(i)
			char = list(self.reference_dic.keys())[position]
			cipher += char

		return cipher


	def decrypt(self, cipher, key):
		cipher = cipher.upper()
		key = key.upper()
		deref = vigenere().dereference(cipher)
		derefer_key = vigenere().dereference(key)
		row_text = []

		for i in range(len(deref)):
			row_text.append((deref[i] - derefer_key[i % len(key)]) % 26 )

		message = ""
		for i in row_text:
			position = list(self.reference_dic.values()).index(i)
			char = list(self.reference_dic.keys())[position]
			message += char

		return message


	def dereference(self, text):
		derefer_str = []
		for i in text:
			derefer_str.append(self.reference_dic[i])

		return derefer_str


if __name__ == "__main__":
	while True:
		control = input("enter encrypt(e)/decrypt(d)/quit(q) : ")
		if control == "q" or control=="Q":
			break
		if control== "e" or control == "E":
			message = input("enter your message : ")
			key = input("enter your key : ")
			cipher = vigenere().encrypt(message, key)
			print(f"{cipher}\n")
		if control == "d" or control == "D":
			cipher = input("enter the cipher : ")
			key = input("enter the key : ")
			message = vigenere().decrypt(cipher, key)
			print(f"{message}\n")


