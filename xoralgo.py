import os


while True:
	mode = input("what do you want encrypt('e')/decrypt('d')/quit('q') : ")
	if mode == "e":
		text = input("text to encrypt : ")
		passwd = input("encryption password : ")
		xor_list = []
		
		#main xor operation are done by this 
		for i in range(len(text)):
			xor_num = ord(text[i]) ^ ord(passwd[i%len(passwd)])
			xor_list.append(xor_num)

		encrypted_text = ''
		for i in xor_list:
			encrypted_text += chr(i)
			
		#write these encrypted string into a file 
		#we can't read or even some ide, command prompt can't show these encrypted values
		#sometimes you can't even copy this text that's why write into a file is important
		with open(f"{os.getcwd()}/encrypt.txt",'w') as file:
			file.write(encrypted_text)
			
		encrypted_text = encrypted_text.encode('ascii')
		print(f"encrypted text is : {encrypted_text}")
		print("this data is just a raw data,\n and not the actuall cipher-text.\ncheck encrypted.txt to see actuall encrypted-text")

	if mode == 'd':
		#just load the cipher text form the file 
		print("loading encrypted_text from encrypt.txt")
		with open(f"{os.getcwd()}/encrypt.txt",'r') as file:
			text = file.read()

		passwd = input("enter password to decrypt : ")
		xor_list = []

		#again doing the same xor operation to get back our real meassage
		for i in range(len(text)):
			xor_num = ord(text[i]) ^ ord(passwd[i%len(passwd)])
			xor_list.append(xor_num)
		
		#load ascii characters form those numbers
		decrypted_text = ''
		for i in xor_list:
			decrypted_text += chr(i)

		print(f"decrypted text is : {decrypted_text}")
		
	if mode == 'q':
		break

