import random 

def play():
    options = ('rock', 'paper', 'scissors')
    
    player = input('Enter your guess: ')
    print(player)
    
    computer_move = random.choice(options)
    print(computer_move)
    
    if player == computer_move:
        print('A tie')
        
    elif player == 'rock'  and  computer_move == 'scissors':
        print('You win')
    
    elif player == 'paper'  and  computer_move == 'rock':
        print('You win')
    
    elif player == 'scissors'  and  computer_move == 'paper':
        print('You win')
        
    else:
        print('You lose')
        
    reset()

def reset():
    reset = input('Restart the game?: ')
    if reset == 'yes':
        play()
    else:
        print('Game over')
        
play()
