#Fancy ASCII text ...
import pyfiglet

print(pyfiglet.figlet_format("Youtube Downloader ", font = "bulbhead" ).center(30))
print(pyfiglet.figlet_format("Created By @FaLLenGuY", font = "digital" ).ljust(30))
print("-"*70,"\n")

# import web library ...
import webbrowser
from pytube import YouTube
# url Formatting ...
#url = input ("Enter the URL of the video : ")

def savenet(url):
    download = url[:12] + "ss" + url[12:]
    print( url[:12] + "ss" + url[12:])

    # open browser to download file ...
    webbrowser.open(download,autoraise = True)


def pytube(url):

    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    stream.download()

def Main():

    url = input ("Enter the Video URL >> ")
    choice = int(input("1: Download with SaveFrom.net\n2: Download with PyTube\n>> "))

    if choice == 1:
        savenet(url)

    elif choice ==2:
        pytube(url)

    else:
        print("Invalid Choice Try Againw..........\n")
        Main()

Main()
