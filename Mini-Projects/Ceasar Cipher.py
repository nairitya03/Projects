import time


def main():
    print ("Welcome! to Ceasar Cipher Encoder - Decoder "
           "\nWhat you want to do? \n(1)Encrypt \n(2)Decrypt ")
    
    choice = int(input(">>>"))
      

## define a function to perform shifting 
 
    def encryption (text , shift=3):
        lower_case_txt = text.lower()
        encrypted_msg = []
    
        for _ in lower_case_txt:
            if _ == " ":
                encrypted_msg.append(" ")
                continue
            new = (((ord(_) - 97) + shift) %26 ) + 97
            encrypted_msg.append(chr(new))
           
        print(f'\nEncrypted Message = {"".join(encrypted_msg)}')
    
        time.sleep(15)

## define function to perform brute force
 
    def decryption(message , Key = ''):
        letters = "abcdefghijklmnopqrstuvwxyz"
        
    
        if Key == '' :
            for key in range(len(letters)):
                deciphered_msg = []
                
                for __ in message:
                    if __ in letters:
                        num = letters.find(__)
                        num = num - key
                    
                        if num <0:
                            num = num + len(letters)
                 
                        deciphered_msg.append(letters[num])
                
                    else:
                        deciphered_msg.append(__)
                
                print(f'key={key} - message = {"".join(deciphered_msg)}')
                
        else:
            deciphered_msg =[]
            for _ in message:
                if _ == " ":
                    deciphered_msg.append(" ")
                    continue
           
                old = (((ord(_) - 97) - int(Key)) % 26 ) + 97
                deciphered_msg.append(chr(old))
           
            print(f'\nDeciphered Message = {"".join(deciphered_msg)}')
    
        time.sleep(15)    
    
            
    def switch(case):
        run=True
        
        while run:
            
            usr_msg = input("Enter the message  >>")
    
            Secret_key = input("Enter the Secret key in 'number' >>")
    
            if case == 1:
        
                encryption(usr_msg , int(Secret_key) )
                run=False
                break
            
            elif case ==2:
        
                decryption(usr_msg , Secret_key)
                run=False
                break
            
            else:
                print("\nError... Invalid Selection !!\n")

                retry =input("\nTry Again ? y/n >> ")
                print("\n")
        
                if retry =='y' or retry =='Y':
                    main()                               
                
                elif retry =='n' or retry =='N':
                    run=False        

#user input message
    switch(choice)

if __name__=='__main__':
    main();
    


        
