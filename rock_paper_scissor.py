import random
rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
paper = ('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
scissor = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
game_images = [rock, paper , scissor]
choice_of_user = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for Scissors.\n"))
print(game_images[choice_of_user])
computer_choice = random.randint(0,2)
print("Computer_choice:")
print(game_images[computer_choice])
if choice_of_user >= 3 or choice_of_user < 0:
    print("You Typed An an valid Value .\n You Lose")
elif choice_of_user == 0 and computer_choice == 2:
    print("You win!")
elif choice_of_user == 2 and computer_choice == 0:
    print("You lose!")
elif computer_choice > choice_of_user:
    print("You lose!")
elif choice_of_user > computer_choice:
    print("You win!")
elif computer_choice == choice_of_user:
    print("It's a draw!")

