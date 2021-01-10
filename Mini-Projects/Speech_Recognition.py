#!/bin/env python3
import speech_recognition as speech

#speech= sp

with speech.Microphone() as source:
    print("Speak Now ...")
    
    audio = speech.Recognizer().listen(source)
    
    try:
        output = speech.Recognizer().recognize_google(audio)
        print("you said >>>{}".format(output))
    except :
        print("I didn't hear ya... Say again")
