from pygame import mixer as mix
import random
import pyfiglet 

# ASCII Text Art
print(pyfiglet.figlet_format("Music Player", font = "bulbhead" ))
print(pyfiglet.figlet_format("Created By @FaLLenGuY", font = "digital" ))
print("-"*70,"\n")

## initialize the pygame mixer
mix.init()

##initialize song list
songs=[]

## user Song list
while True:
        print("Add Song ")
        songs.append(input()+".mp3")
        add=input("ADD more songs! Y/N ")
        if add=='y':
                pass
        elif add=='n':
                break
        else:
                print("invalid Choice ")


## Sbuffle function to Add shuffle feature in Music Player
def shuffle():
        choice = input ("Do you want to shuffle the list? y/n ")
        if choice=='y':
                return random.shuffle(songs)            ##random shuffle of songs
        elif choice =='n':
                pass


## A Fucntion to start playing playlist
def play():
        shuffle()                                       ##shuffle call
        

        print("Playing",songs)
        index = 0
        while True:
                if index<len(songs):
                        mix.music.load(songs[index])
                        mix.music.set_volume(1)
                        mix.music.play()
                        index += 1
                else:
                        print("End of the Playlist")
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



