import random

def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

def print_hand(hand, name='Guest'):
    hands = ['Rock', 'Paper', 'Scissors']
    print(name + ' picked: ' + hands[hand])

def judge(player, computer):
    if player == computer:
        return 'Draw'
    elif player == 0 and computer == 1:
        return 'Lose'
    elif player == 1 and computer == 2:
        return 'Lose'
    elif player == 2 and computer == 0:
        return 'Lose'
    else:
        return 'Win'


    
print("#############################################################################")

print('Starting the Rock Paper Scissors game!')

player_name = input('Please enter your name: ')

loop = True

while loop:
    print("------------------------------------------------------------------")
    
    print('Pick a hand: (0: Rock, 1: Paper, 2: Scissors)')
    player_hand = int(input('Please enter a number (0-2): '))

    if validate(player_hand):
    # Assign a random number between 0 and 2 to computer_hand using randint
        computer_hand = random.randint(0,2) 
    
        print_hand(player_hand, player_name)
        print_hand(computer_hand, 'Computer')

        result = judge(player_hand, computer_hand)
        print('Result: ' + result)
        choice = input("Want to continue? y/n :")
        if choice == 'n' or choice == 'N':
            loop = False
        else:
            continue
        
    else:
        print('Please enter a valid number')

print("Thanks for Playing !! See you next time.")   













    
