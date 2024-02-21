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

my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0,2)

game_images = [rock, paper, scissors] # 배열로 정보 담는다 

if my_choice < 0 or my_choice >= 3: # 0~2 숫자가 아닐때 오류 
  print("you have to enter the number 0~2")
else: # 0~2 숫자 일 때 
  print(f"{game_images[my_choice]}\n {game_images[computer_choice]}")
  if my_choice == 0 and computer_choice == 2:
    print("you win")
  elif my_choice < computer_choice:
    print("you lose")
  elif my_choice == 2 and computer_choice == 0:
    print("you lose")
  elif my_choice > computer_choice:
    print("you win")
  elif my_choice == computer_choice:
    print("you draw")
