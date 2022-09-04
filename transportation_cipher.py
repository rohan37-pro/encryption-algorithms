import random


def encrypt(plain_text, m):
	key = get_key(m)
	print(f"your key is {key}")
	text_list = devide_into_win_size(plain_text,m)
	cipher = permute(text_list,key)
	cipher = "".join(cipher)
	return cipher


def permute(text, key):
	cipher = []
	for i in text:
		for j in range(len(i)):
			cipher.append(i[key[j]-1])
	return cipher


def devide_into_win_size(text,w):
	windows = len(text)//w
	if len(text)%w != 0:
		windows	+=1

	text_list = []
	for i in range(windows):
		text_list.append(text[ i*w : (i+1)*w ])

	while len(text_list[-1])<w:
		text_list[-1]+="X"
	return text_list


def get_key(m):
	num_list = []
	for i in range(1,m+1):
		num_list.append(i)

	key_list = []

	for i in range(m):
		k = random.choice(num_list)
		key_list.append(k)
		num_list.remove(k)
	return key_list


def decrypt(cipher, key):
	m = len(key)
	cipher_list = devide_into_win_size(cipher,m)
	text_list = reverse_permute(cipher_list,key)
	message = "".join(text_list)
	return message


def reverse_permute(text_list, key):
	text = []
	for i in text_list:
		for j in range(len(i)):
			text.append(i[key.index(j+1)])
			
	return text


if __name__ == "__main__":
	cli = ""
	while True:
		cli = input("encrypt(e)/decrypt(d)/quit(q)")
		if cli=="e" or cli=="E":
			message = input("enter message to encrypt : ")
			winsize = int(input("enter window size : "))
			cipher = encrypt(message,winsize)
			print(f"the cipher is : {cipher}")
		if cli == "d" or cli=="D":
			cipher = input("enter cipher : ")
			key = eval(input("enter key : "))
			message = decrypt(cipher, key)
			print(f"the message is : {message}")
		if cli=="q" or cli=="Q":
			break
			