# ==============================================
# Rock Paper Scissors Lizard Spock (for Codedex)
#===============================================

# 1) ✊
# 2) ✋
# 3) ✌️
# 4) 🦎
# 5) 🖖

import random

player = int(input("Pick a number between 1 - 5: "))
computer = random.randint(1, 5)

# You win! ↓

if player == 1  and computer == 3:
    print("You chose ✊ and CPU chose ✌️. You win!")
elif player == 2 and computer == 1:
    print("You chose ✋ and CPU chose ✊. You win!")
elif player == 3 and computer == 2:
    print("You chose ✌️ and CPU chose ✋. You win!")
elif player == 1 and computer == 4:
    print("You chose ✊ and CPU chose 🦎. You win!")
elif player == 4 and computer == 5:
    print("You chose 🦎 and CPU chose 🖖. You win!")
elif player == 5 and computer == 3:
    print("You chose 🖖 and CPU chose ✌️. You win!")
elif player == 3 and computer == 4:
    print("You chose ✌️ and CPU chose 🦎. You win!")
elif player == 4 and computer == 2:
    print("You chose 🦎 and CPU chose ✋. You win!")
elif player == 2 and computer == 5:
    print("You chose ✋ and CPU chose 🖖. You win!")
elif player == 5 and computer == 1:
    print("You chose 🖖 and CPU chose ✊. You win!")

    
# It's a tie! ↓
    
elif player == 1 and computer == 1:
    print("You and CPU chose ✊ It's a tie!.")
elif player == 2 and computer == 2:
    print("You and CPU chose ✋ It's a tie!.")
elif player == 3 and computer == 3:
    print("You and CPU chose ✌️ It's a tie!.")
elif player == 4 and computer == 4:
    print("You and CPU chose 🦎 It's a tie!.")
elif player == 5 and computer == 5:
    print("You and CPU chose 🖖 It's a tie!.")
    
# You lose! ↓
    
elif player == 3 and computer == 1:
    print("You chose ✌️ and CPU chose ✊. You lose!")
elif player == 1 and computer == 2:
    print("You chose ✊ and CPU chose ✋. You lose!")
elif player == 2 and computer == 3:
    print("You chose ✋ and CPU chose ✌️. You lose!")
elif player == 4 and computer == 1:
    print("You chose 🦎 and CPU chose ✊. You lose!")
elif player == 5 and computer == 4:
    print("You chose 🖖 and CPU chose 🦎. You lose!")
elif player == 3 and computer == 5:
    print("You chose ✌️ and CPU chose 🖖. You lose!")
elif player == 4 and computer == 3:
    print("You chose 🦎 and CPU chose ✌️. You lose!")
elif player == 2 and computer == 4:
    print("You chose ✋ and CPU chose 🦎. You lose!")
elif player == 5 and computer == 2:
    print("You chose 🖖 and CPU chose ✋. You lose!")
elif player == 1 and computer == 5:
    print("You chose ✊ and CPU chose 🖖. You lose!")  
else: 
    print("Invalid input! Pick a number between 1 - 5:. ")

   