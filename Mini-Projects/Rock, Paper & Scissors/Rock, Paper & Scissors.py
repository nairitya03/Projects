#Fancy ASCII text ...
import pyfiglet

print(pyfiglet.figlet_format("Rock, Paper & Scissors", font = "bulbhead" ).center(30))
print(pyfiglet.figlet_format("Created By @FaLLenGuY", font = "digital" ).ljust(30))
print("-"*70,"\n")

#import radom library ...
import random

#
def validate(hand):
    if hand < 1 or hand > 3:
        return False
    return True

def print_hand(hand, name='Guest'):
    hands = ['Rock', 'Paper', 'Scissors']
    print(name + ' picked: ' + hands[hand-1])

def judge(player, computer):
    if player == computer:
        return 'Draw'
    elif player == 1 and computer == 2:
        return 'Lose'
    elif player == 2 and computer == 3:
        return 'Lose'
    elif player == 3 and computer == 1:
        return 'Lose'
    else:
        return 'Win'


    
print("#############################################################################")

print('Starting the Rock Paper Scissors game!')

player_name = input('Please enter your name: ')

loop = True

while loop:
    print("------------------------------------------------------------------")
    
    print('Pick a hand: (1: Rock, 2: Paper, 3: Scissors)')
    player_hand = int(input('Please enter a number (1-3): '))

    if validate(player_hand):
    # Assign a random number between 0 and 2 to computer_hand using randint ...
        computer_hand = random.randint(1,3) 
    
        print_hand(player_hand, player_name)
        print_hand(computer_hand, 'Computer')

        result = judge(player_hand, computer_hand)
        print('Result: ' + result)
        choice = input("\nWant to continue? y/n :")

        if choice == 'n' or choice == 'N':
            loop = False
                                
        elif choice == 'y' or choice == 'Y':
            continue
         
    else:
        print('Please enter a valid number')

print("Thanks for Playing !! See you next time.")   













    
