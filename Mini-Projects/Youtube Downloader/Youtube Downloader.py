#Fancy ASCII text ...
import pyfiglet

print(pyfiglet.figlet_format("Youtube Downloader ", font = "bulbhead" ).center(30))
print(pyfiglet.figlet_format("Created By @FaLLenGuY", font = "digital" ).ljust(30))
print("-"*70,"\n")

# import web library ...
import webbrowser

# url Formatting ...
url = input ("Enter the URL of the video : ")

download = url[:12] + "ss" + url[12:]
print( url[:12] + "ss" + url[12:])

# open browser to download file ...
webbrowser.open(download,autoraise = True)


