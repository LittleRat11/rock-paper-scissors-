import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock, paper, scissors]
# User Side
user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scisscors.")
)
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print("User")
    print(game_images[user_choice])
    # Computer side
    print("Computer \n")
    computer_choice = random.randint(0, 2)
    print(game_images[computer_choice])
    # Win or lose

    if user_choice == 0 and computer_choice == 2:
        print("User Win")
    elif user_choice == 1 and computer_choice == 0:
        print("User Win")
    elif user_choice == 2 and computer_choice == 1:
        print("User Win")
    elif user_choice == computer_choice:
        print("Draw")
    else:
        print("Computer Win")
