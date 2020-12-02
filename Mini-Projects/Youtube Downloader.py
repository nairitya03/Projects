import webbrowser

url = input ("Enter the URL of the video : ")
#url ='https://www.youtube.com/watch?v=mPhboJR0Llc&list=RDYPohR_9v6HA&index=4'
download = url[:12] + "ss" + url[12:]
print( url[:12] + "ss" + url[12:])
webbrowser.open(download,autoraise = True)


