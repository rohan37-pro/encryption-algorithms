ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
char = "+/"

base64 = {}

for i in range(64):
	bit6 = bin(i).split("0b")[1]
	if len(bit6) < 6:
		bit6 = '0'*(6-len(bit6)) + bit6
	if i<= 25:
		base64[ALPHA[i]] = bit6
	if 25<i<=51:
		base64[alpha[i-26]] = bit6
	if 51<i<=61:
		base64[num[i-52]] = bit6
	if 61<i<=63:
		base64[char[i-62]] = bit6

def binarytodecimal(number):
	decimal = 0
	pow = 0
	for i in range(-1,-len(number)-1,-1):
		decimal += int(number[i])*(2**pow)
		pow+=1
	return decimal


while True:
	mode = input("what do you want encrypt(e)/decrypt(d)/quit(q) : ")

	if mode == "e":
		text = input("text to encrypt : ")
		binary = ""

		for i in text:
			ASCII = ord(i)
			val = bin(ASCII).split("0b")[1]
			binary += '0'*(8-len(val)) + val

		reminder = len(binary)%6
		div = len(binary)//6
		bin_list = []

		if reminder!=0:
			for i in range(div+1):
				bin_item = binary[i*6:6*(i+1)]
				if len(bin_item) < 6:
					bin_item += '0'*(6-reminder)
				bin_list.append(bin_item)

		else:
			for i in range(div):
				bin_item = binary[i*6:6*(i+1)]
				bin_list.append(bin_item)

		encrypted_text = ""
		for i in bin_list:
			for j in base64:
				if int(base64[j]) == int(i):
					encrypted_text += j

		if reminder != 0:
			encrypted_text += "="*((6-reminder)//2)
		print(encrypted_text)

	if mode == "d":
		text = input("text to decrypt : ")
		reminder = text.count("=")*2
		decrypt_list = []

		for i in text:
			if i!='=':
				decrypt_list.append(base64[i])
		
		decrypt_list[-1] = decrypt_list[-1][0:-reminder]
		decrypt_byte = ''

		for i in decrypt_list:
			decrypt_byte += i 

		decrypted_text = ''
		div = len(decrypt_byte)//8
		for i in range(div):
			byte = decrypt_byte[i*8:8*(i+1)]
			decrypted_text += chr(binarytodecimal(byte))

		print(decrypted_text)

	if mode == 'q':
		break

