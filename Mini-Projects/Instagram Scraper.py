import requests 
from bs4 import BeautifulSoup as BS
import time 

begin = time.time() 
url = "https://www.Instagram.com/{}/"

def scrape (username):
    full_url = url.format(username) 
    r = requests.get(full_url)
    s = BS(r.text,"lxml")
    
    tag = s.find("meta",attrs ={"name":"description"})
    text = tag.attrs['content']
    main_text = text.split("-")[0]
    
    return main_text


username = input("enter username :")
data =scrape (username)

end = time.time() 
time_loop = int(end-begin)
i=0
while (i<time_loop):
    print("#"*i,end="\r")
    time.sleep(1)
    i+=1

print ("\n\n",data)



  
