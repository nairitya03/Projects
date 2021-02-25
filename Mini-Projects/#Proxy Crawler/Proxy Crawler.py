from bs4 import BeautifulSoup as bs
import requests
import time

def crawler():
    proxies = []
    links = input("Enter the Url >>>")
    
    r = requests.get(links)
    s = bs(r.text,"html.parser")
    
    for i in s.find_all("tr")[:30]:
        try:
            data = i.find_all("td")
            address = data[0].text
            port = data[1].text
            type_ = data[4].text
            proxy = address +":"+ port
            proxies.append({"https":proxy})
        
        except :
            pass
        
    return proxies

proxies = crawler()
print(proxies,"\n")

time.sleep(15)
