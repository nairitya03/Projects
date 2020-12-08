##import webbrowser library 
import webbrowser


##define a funtion for switching b/w Search Engines
def engine(i):
        switcher={
                0:'https://www.google.com/search?sxsrf=ALeKk02WpG_IOqTkcPSjQC671SYga4IRsQ%3A1606904539348&source=hp&ei=22rHX-GfEvrA3LUPxvqaaA&q=',
                1:'https://duckduckgo.com/?q=',
                2:'https://www.bing.com/search?q=hel',
               
             }
        return switcher.get(i,"Invalid Search Engine")


## User input for Favourite Search Engine 
engine_num = int(input ("Enter your Search Engine"
              "\n 0: Google"
              "\n 1: DuckDuckGo"
              "\n 2: Bing"
              "\n >>>"
              ))



## User input for Search String
keyword = input ("Enter the Search Keyword:- ")


## Forming search URL
search = engine(engine_num) + keyword

#print(search)

## print message
print("Searching Web for "+ keyword )

##funtion call t0 open search in native browser
webbrowser.open(search, autoraise = True)

