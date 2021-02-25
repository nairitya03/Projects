#Fancy ASCII text ...
import pyfiglet

print(pyfiglet.figlet_format("Speech Rec. ", font = "bulbhead" ).center(30))
print(pyfiglet.figlet_format("Created By @FaLLenGuY", font = "digital" ).ljust(30))
print("-"*60,"\n")

import speech_recognition as speech

#speech= sp

with speech.Microphone() as source:
    print("\nSpeak Now ...")
    
    audio = speech.Recognizer().listen(source)
    
    try:
        output = speech.Recognizer().recognize_google(audio)
        print("\nYou said >>> {}".format(output))
    except :
        print("\nI didn't hear ya... Say again!!!")
