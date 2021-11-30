

class caesar_cipher:


	def encrpt_a2z(text,shift):
		cipher = ""
		for i in text:
			if (65<=ord(i)<=90) or (97<=ord(i)<=122):
				if i.isupper():
					ciph_char = chr( (ord(i)+shift - 65)%26 + 65 )
					cipher += ciph_char
				if i.islower():
					ciph_char = chr( (ord(i)+shift - 97)%26 + 97)
					cipher += ciph_char
			else:
				cipher += i
		return cipher



	def decrpt_a2z(cipher,shift):
		text = ""
		for i in cipher:
			if (65<=ord(i)<=90) or (97<=ord(i)<=122):
				if i.isupper():
					ciph_char = chr( (ord(i)-shift - 65)%26 + 65 )
					text += ciph_char
				if i.islower():
					ciph_char = chr( (ord(i)-shift - 97)%26 + 97)
					text += ciph_char
			else:
				text += i

		return text




	def encrypt_ASCII(text,shift):
		cipher = ""

		for i in text:
			ciph_char = chr( ord(i)+shift )
			cipher += ciph_char

		return cipher


	def decrypt_ASCII(cipher,shift):
		text = ""

		for i in cipher:
			ciph_char = chr( ord(i)-shift )
			text += ciph_char

		return text


	def rot13(string):
		cipher = ""
		for i in text:
			if (65<=ord(i)<=90) or (97<=ord(i)<=122):
				if i.isupper():
					ciph_char = chr( (ord(i)+13 - 65)%26 + 65 )
					cipher += ciph_char
				if i.islower():
					ciph_char = chr( (ord(i)+13 - 97)%26 + 97)
					cipher += ciph_char
			else:
				cipher += i

		return cipher


