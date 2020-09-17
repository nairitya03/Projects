user_input =  'random'

data = []

def Menu():
    print ("MENU")
    print ("1.Add an item")
    print ("2.Mark as Done")
    print ("3.See the to do list")
    print ("4.EXIT")


while user_input !=4:
    Menu()

    user_input=int(input("Enter your choice >>"))

    if user_input ==1:
        item=input ("Add an item >>")
        data.append(item)
        print ("Item Added :",item)
        
    elif user_input ==2:
        item = input("Mark item as Done >>")
        data.remove(item)
        print (item,"Marked as Done")
        
    elif user_input ==3:
        print (data)

    elif user_input == 4:
        break

    else :
        print ("please enter again")
    

print ("GoodBye........")

