import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])
if user_choice >= 3 or user_choice< 0:
  print ("you have typed invalid number. You Lose!")
elif user_choice==0 and computer_choice==2:
  print("You Won")
elif computer_choice==0 and user_choice==2:
  print("You Lose")
elif user_choice>computer_choice:
  print("You won")
elif computer_choice > user_choice:
  print("You Lose")
elif user_choice==computer_choice:
  print("Its Draw")
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.