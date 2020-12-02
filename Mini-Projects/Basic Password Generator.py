import random
import time
 
size = int(input("enter the size of PASSWORD: "))

list1 = ['1','2','3','4','5','6','7','8','9']
list2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list3 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Z','Z']
list4 = ['!','@','#','$','%',';','&','*',';','<','>','?','/','|']
combination = list2 + list1 + list4 + list3

otp=[]
otp=''.join(random.sample(combination,size))
print (otp)

time.sleep(45)
