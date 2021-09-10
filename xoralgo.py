import os


while True:
	mode = input("what do you want encrypt('e')/decrypt('d')/quit('q') : ")
	if mode == "e":
		text = input("text to encrypt : ")
		passwd = input("encryption password : ")
		xor_list = []

		for i in range(len(text)):
			xor_num = ord(text[i]) ^ ord(passwd[i%len(passwd)])
			xor_list.append(xor_num)

		encrypted_text = ''
		for i in xor_list:
			encrypted_text += chr(i)

		with open(f"{os.getcwd()}/encrypt.txt",'w') as file:
			file.write(encrypted_text)

		print(f"encrypted text is : {encrypted_text}")
		print("open the text file to view the encrypted text")

	if mode == 'd':

		print("loading encrypted_text from encrypt.txt")
		with open(f"{os.getcwd()}/encrypt.txt",'r') as file:
			text = file.read()

		passwd = input("enter password to decrypt : ")
		xor_list = []

		
		for i in range(len(text)):
			xor_num = ord(text[i]) ^ ord(passwd[i%len(passwd)])
			xor_list.append(xor_num)

		decrypted_text = ''
		for i in xor_list:
			decrypted_text += chr(i)

		print(f"decrypted text is : {decrypted_text}")
		
	if mode == 'q':
		break

