import requests 
from bs4 import BeautifulSoup as BS
import time

#Fancy ASCII Text ...
import pyfiglet 

print(pyfiglet.figlet_format("Insta Scraper", font = "bulbhead" ))
print(pyfiglet.figlet_format("Created By @FaLLenGuY", font = "digital" ))
print("-"*70,"\n")

# time counter ...
begin = time.time() 
url = "https://www.instagram.com/{}"

# Scrape Funtion ...
def scrape (username):
    full_url = url.format(username) 
    r = requests.get(full_url)
    s = BS(r.text,"lxml")
    
    tag = s.find("meta",attrs ={"name":"description"})
    text = tag.attrs['content']
    main_text = text.split("-")[0]
    
    return main_text


username = input("Enter Username >>> ")
data = scrape (username)

end = time.time() 
time_loop = int(end-begin)
i=0

# time loop ...
while (i<time_loop):
    print(f"{i}%",end="\r")
    time.sleep(1)
    i+=1

print ("\n",data)

time.sleep(20)
  
