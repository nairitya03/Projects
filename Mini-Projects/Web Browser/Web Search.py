#Fancy ASCII text ...
import pyfiglet

print(pyfiglet.figlet_format("Web Search", font = "bulbhead" ).center(30))
print(pyfiglet.figlet_format("Created By @FaLLenGuY", font = "digital" ).ljust(30))
print("-"*70,"\n")


# import webbrowser library ...
import webbrowser


# Define a funtion for switching b/w Search Engines ...
def engine(i):
        switch={
                1:'https://www.google.com/search?sxsrf=ALeKk02WpG_IOqTkcPSjQC671SYga4IRsQ%3A1606904539348&source=hp&ei=22rHX-GfEvrA3LUPxvqaaA&q=',
                2:'https://duckduckgo.com/?q=',
                3:'https://www.bing.com/search?q=',
                4:'https://in.search.yahoo.com/search?p='
               
             }
        return switch.get(i,"Invalid Search Engine")

# User input for Favourite Search Engine ... 
engine_num = int(input ("Enter your Search Engine"
              "\n 1: Google"
              "\n 2: DuckDuckGo"
              "\n 3: Bing"
              "\n 4: Yahoo"
              "\n >> "
              ))



#  User input for Search String ...
keyword = input ("Enter the Search Keyword:- ")


        #  Forming search URL ...
search = engine(engine_num) + keyword

        #print(search)

        #  print message ...
print("Searching Web for "+ keyword )

        # funtion call to open search in native browser ...
webbrowser.open(search, autoraise = True)

