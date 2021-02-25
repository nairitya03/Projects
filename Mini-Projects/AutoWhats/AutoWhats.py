import pywhatkit
import time

#Fancy ASCII Text ...
import pyfiglet 

print(pyfiglet.figlet_format("AutoWhats", font = "bulbhead" ))
print(pyfiglet.figlet_format("Created By @FaLLenGuY", font = "digital" ))
print("-"*70,"\n")

def sendmsg():

    ##enter the mobile number of reciver With contry code
    mob_no= input("input you moblie number with country code \n >>")

    ##enter the message to be sent
    msg = input( "Enter the message\n >>")

    ##Time assigning
    hr,mint = map(int, input("Enter Time In HH:MM {24hr format} \n >>").strip().split(':'))

    ##funtion definition
    pywhatkit.sendwhatmsg(mob_no, msg, hr, mint)



def history():
    
    ##Display information of all the messages sent.
    pywhatkit.showHistory()

if __name__=='__main__':

    print("------------------------------------------\n")
    choice=int(input("Enter your Search Engine"
              "\n 1: Send Message"
              "\n 2: Show History"
              "\n >>>"
              ))
    if choice==1:
        sendmsg()

    elif choice==2:
        history()
        time.sleep(200)

    else:
        print("Invalid Choice!! ")
   
    
