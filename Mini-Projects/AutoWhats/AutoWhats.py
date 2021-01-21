import pywhatkit


##enter the mobile number of reciver With contry code
mob_no= input("input you moblie number with country code \n >>")


##enter the message to be sent
msg = input( "Enter the message\n >>")


##Time assigning
hr,mint = map(int, input("Enter Time In HH:MM {24hr format} \n >>").strip().split(':'))


##funtion definition
pywhatkit.sendwhatmsg(mob_no, msg, hr, mint)
