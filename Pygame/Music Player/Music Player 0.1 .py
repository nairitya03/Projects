from pygame import mixer as mix
import random

## initialize the pygame mixer
mix.init()

## user Song list
songs = ["sample\Drag_me_Down.mp3","sample\Everybody.mp3","sample\Legends_never_die.mp3","sample\Taaron.mp3","sample\Vaaste.mp3"]

## Sbuffle function to Add shuffle feature in Music Player
def shuffle():
        choice = input ("Do you want to shuffle the list? y/n ")
        if choice=='y':
                
                 ##random shuffle of songs
                return random.shuffle(songs)           
        elif choice =='n':
                pass

## A Fucntion to start playing playlist
def play():
        
        ## Call Shuffle Funtion
        shuffle()                                       
        index = 0
        while True:
                if index<len(songs):
                        mix.music.load(songs[index])
                        mix.music.set_volume(1)
                        mix.music.play()
                        index += 1
                else:
                        print("End of the list")
                        break
        
                while True:
                        query = input("  Press 'P' to pause and Press 'R' to resume \n  Press 'N' for next song \n  Press 'E' exit player \n>>>")

                        if (query == 'p'):
                                mix.music.pause()
                        elif (query =='r'):
                                mix.music.unpause()
                        elif (query =='n'):
                                mix.music.stop()
                                break
                        if (query == 'e'):
                                quit()

play()



