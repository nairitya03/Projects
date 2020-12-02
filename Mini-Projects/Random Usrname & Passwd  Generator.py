import random
import time
#import string 
size = int(input("enter the size of CREDENTIALS : "))
list1 = ['1','2','3','4','5','6','7','8','9']
list2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list3 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Z','Z']
list4 = ['!','@','#','$','%',';','&','*',';','<','>','?','/','|']
password = list2 + list1 + list4 + list3
username = list2+list3

#Random UserName
usrname = []
usrname=''.join(random.sample(username,size))
print("USERNAME : ",usrname)

#Random Password
passwd = []
passwd=''.join(random.sample(password,size))
print ("PASSWORD : ",passwd)

time.sleep(45)

