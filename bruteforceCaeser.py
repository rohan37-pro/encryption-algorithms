

cip = input("enter cipher: ")
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(1,26):
    plaintext = ''
    for c in cip:
        if c!=' ':
            plaintext+=letters[(letters.index(c)+i)%26]
        else:
            plaintext+=' '
    print(plaintext)
