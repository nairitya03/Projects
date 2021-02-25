import time
import pyfiglet

#Fancy ASCII text
print(pyfiglet.figlet_format("Email Extractor", font = "bulbhead" ).center(30))
print(pyfiglet.figlet_format("Created By @FaLLenGuY", font = "digital" ).ljust(30))
print("-"*70,"\n")

# funtion to countdown time
def countdown(t):
    while t:
        mins,secs = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end='\r')
        time.sleep(1)
        t-= 1
        
    print("Trigger Some Task...")
    time.sleep(10)

#constructor initializes
if __name__=='__main__':
    
    t=input ("Enter time in seconds >> ")
    countdown(int(t))
