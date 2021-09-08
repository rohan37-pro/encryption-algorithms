while True:
    mode = input("what do you want decrypt(d)/encrypt(e)/exit(q) : ")
    
    if mode=="e":
        text = input("enter a text to encrypt : ")
        shift = int(input("Enter the shift value : "))
        new_text = ''
        for i in text:
            num = ord(i)
            new_text += chr(num+shift)
        print(f"encrypted text is : {new_text}")
        
    if mode == "d":
        text = input("enter a text to decrypt : ")
        shift = int(input("Enter the shift value : "))
        new_text = ''
        for i in text:
            num = ord(i)
            new_text += chr(num-shift)
        print(f"decrypted text is : {new_text}")

    if mode =="q":
        break
