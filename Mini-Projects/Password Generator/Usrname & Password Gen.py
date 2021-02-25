# import Libraries ...
import random
import time

#Fancy ASCII text...
import pyfiglet

print(pyfiglet.figlet_format("Password & Username Gen", font = "bulbhead" ).center(30))
print(pyfiglet.figlet_format("Created By @FaLLenGuY", font = "digital" ).ljust(30))
print("-"*70,"\n")

# Create Character set ... 
size = int(input("Enter the size of CREDENTIALS : "))
list1 = ['1','2','3','4','5','6','7','8','9']
list2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list3 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Z','Z']
list4 = ['!','@','#','$','%',';','&','*',';','<','>','?','/','|']
password = list2 + list1 + list4 + list3
username = list2+list3

#Random UserName Genrator ...
usrname = []
usrname=''.join(random.sample(username,size))
print("\nUSERNAME : ",usrname)

#Random Password Genrator ...
passwd = []
passwd=''.join(random.sample(password,size))
print ("\nPASSWORD : ",passwd)

time.sleep(45)

