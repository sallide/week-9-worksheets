
import sys
import random

options = ['rock','paper','scissors']

if len(sys.argv) > 1 :        
    player = sys.argv[1]
    print(f"You: {player}")
else :
    player = ' '

computer = random.choice(options)
print(f"Computer: {computer}")

if player == computer :
    print(f"Draw")
elif player == options[(options.index(computer)+1)%3] :
    print(f"You won")
elif player == options[(options.index(computer)-1)%3] :
    print(f"You lost")
else :
    print(f"Invalid choice - you lose")
