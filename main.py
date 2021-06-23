import random
import os

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
rps = [rock, paper, scissors]

os.system('clear') or None #clear console
print("\t\tWelcome to Rock-Paper-Scissors game!\n ")
#User's choice 
user_choice = int( input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ") )
#Computer's random choice
computer_choice = random.randint(0, 2)

os.system('clear') or None #clear console
#User chooses rock
if user_choice == 0:

  #print user's choice
  print(f"\nYour choice: \n{rps[0]}")

  #Check winner if user chooses rock:

  #Rock vs Rock
  if computer_choice == 0:
    print(f"\nComputer's choice: \n{rps[0]}")
    print("\nIt's a draw.")

  #Rock vs Paper
  elif computer_choice == 1:
    print(f"\nComputer's choice: \n{rps[1]}")
    print("\nYou lost.")

  #Rock vs Scissors  
  elif computer_choice == 2:
    print(f"\nComputer's choice: \n{rps[2]}")
    print("\nYou won.")

#User chooses paper
elif user_choice == 1:

  #Print user's choice
  print(f"Your choice: \n{rps[1]}")

  #Check winner if user chooses paper
  #Paper vs Rock
  if computer_choice == 0:
    print(f"\nComputer's choice: \n{rps[0]}")
    print("\nYou won.")

  #Paper vs Paper
  elif computer_choice == 1:
    print(f"\nComputer's choice: \n{rps[1]}")
    print("\nIt's a draw.")

  #Paper vs Scissors
  elif computer_choice == 2:
    print(f"\nComputer's choice: \n{rps[2]}")
    print("\nYou lost.")

#User chooses scissors
elif user_choice == 2:

  #Print user's choice
  print(f"Your choice: \n{rps[2]}")

  #Scissors vs Rock
  if computer_choice == 0:
    print(f"\nComputer's choice: \n{rps[0]}")
    print("\nYou lost.")

  #Scissors vs Paper  
  elif computer_choice == 1:
    print(f"\nComputer's choice: \n{rps[1]}")
    print("\nYou won.")

  #Scissors vs Scissors
  elif computer_choice == 2:
    print(f"\nComputer's choice: \n{rps[2]}")
    print("\nIt's a draw.")

#User types an invalid number    
else:
  print("You typed an invalid number, run again.")
