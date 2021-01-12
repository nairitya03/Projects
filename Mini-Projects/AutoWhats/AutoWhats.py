import pywhatkit


##enter the mobile number of reciver With contry code
mobno= input("input you moblie number with country code \n >>")


##enter the message to be sent
message = input( "Enter the message\n >>")


##Time assigning
hr,mint = map(int, input("Enter Time In HH:MM {24hr format} \n >>").strip().split(':'))


##funtion definition
pywhatkit.sendwhatmsg(mobno, message, hr, mint, wait_time=3)
