import pygame
from gtts import gTTS

pygame.mixer.init()

def convertToAudio(audioName, input_string):

    gtts_obj = gTTS( text= input_string,tld='com',lang='en')
    
    gtts_obj.save("Speaky-"+ audioName)
    
    print("\nAudio Saved successfully !")
    
    pygame.mixer.music.load("Audio_Bot-"+ audioName)
    
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        continue
    
if __name__ == '__main__':

    audioFilename = input("\nName for the Audio file >> ")+".mp3"
    
    inputString = input("\nString to be saved as audio >> ")
        
    convertToAudio(audioFilename,inputString)
