#import libraries ...
import random
import time

#Fancy ASCII text...
import pyfiglet

print(pyfiglet.figlet_format("Password Genrator", font = "bulbhead" ).center(30))
print(pyfiglet.figlet_format("Created By @FaLLenGuY", font = "digital" ).ljust(30))
print("-"*70,"\n")

# Create characte set ...
size = int(input("Enter the size of PASSWORD: "))

list1 = ['1','2','3','4','5','6','7','8','9']
list2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list3 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Z','Z']
list4 = ['!','@','#','$','%',';','&','*',';','<','>','?','/','|']
combination = list2 + list1 + list4 + list3

# Radom Genrator ...
password=[]
password=''.join(random.sample(combination,size))
print (password)

time.sleep(25)
