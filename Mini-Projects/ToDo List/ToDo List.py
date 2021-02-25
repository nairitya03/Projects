#Fancy ASCII text ...
import pyfiglet

print(pyfiglet.figlet_format("ToDo List !", font = "bulbhead" ).center(30))
print(pyfiglet.figlet_format("Created By @FaLLenGuY", font = "digital" ).ljust(30))
print("-"*70,"\n")

import time


# simple To DO list ...


user_input =  'random'
Null=[]
data = []

# define menu function ...
def Menu():
    print ("\n------  MENU  --------\n")
    print ("1. Add an Item.")
    print ("2. Remove an Item.")
    print ("3. See the to do list.")
    print ("4. EXIT")

#take user input and loop
while user_input !=4:
    Menu()

    user_input=input("\nEnter your choice >>>")

    if user_input.isnumeric()==True:

        if int(user_input) ==1:
            item=input ("Add an item >>>")
            data.append(item)
            print ("\nItem Added :",item)
            
        elif int(user_input) ==2:
            item = input("Remove an Item >>")
            data.remove(item)
            print (item,"Removed !\n")
            
        elif int(user_input) ==3:

            if data == Null:
                print ("\nList Empty!! Add Some Items ...")

            else:
                for i, item in enumerate(data, start=1):
                    print(i,item)
                    
                time.sleep(3)
                
        elif int(user_input) == 4:
            break

        else :
            print ("\nInvalid Choice!! Please enter again ...")
    else :
        print ("\nInvalid Choice!! Please enter again ...")
    

print ("\n------  Good Bye !!  --------")
time.sleep(2)

