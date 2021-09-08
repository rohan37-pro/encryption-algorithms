while True:
    #the mode variable stores your choice. 
    mode = input("what do you want decrypt(d)/encrypt(e)/exit(q) : ")
    
    if mode=="e":
        #first it takes the text you wanna encrypt
        text = input("enter a text to encrypt : ")
        #then it takes the shift value which is used just to make it harder for someone to guess the actual shift
        shift = int(input("Enter the shift value : "))
        #empty string to store the encypted characters in the for loop below
        new_text = ''
        for i in text:
            #ord to convert a character into its unicode code
            num = ord(i)
            #adding the shift value which is an int , with the unicode code of the character which will give us a whole new character
            new_text += chr(num+shift)
        #finally printing the encrypted value
        print(f"encrypted text is : {new_text}")
     
    #'d' for decrypting which is pretty much same as the encryption part soo, no brainer
    if mode == "d":
        text = input("enter a text to decrypt : ")
        shift = int(input("Enter the shift value : "))
        new_text = ''
        for i in text:
            num = ord(i)
            new_text += chr(num-shift)
        print(f"decrypted text is : {new_text}")
    #finally mode 'q' to quit
    if mode =="q":
        break
