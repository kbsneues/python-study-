# 유효범위 개념 

# Local scope 지역 범위 -> 함수 안에 설정한 변수 

# global scope 전역 범위 -> 함수 외부에 설정한 변수 , 파일 내부 어디에서나 사용 가능 

# namespace 이름 공간 

# 블록 범위 

# 글로벌 변수 global 키워드 , 대문자로 많이 사용 

from art import logo

print(logo)

import random

answer = random.randint(1, 100) # 1~100 사이의 난수 

print(f"Pseet, the correct answer is {answer}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def game(repeat):
  for attempts in range(repeat,0,-1):
    print(f"You have {attempts} remaining to guess the number.")
    user_answer = int(input("Make a guess: "))
    if user_answer > answer: # 정답보다 클 때 
      print("Too high.\nGuess again.") 
    elif user_answer < answer: # 정답보다 작을 때 
      print("Too low.\nGuess again.")
    else:
      print(f"You got it! The answer was {answer}") # 정답과 같을 때 
      break
  print("Game over")

if difficulty == "easy":  
  game(10) # 기회 10번 
elif difficulty == "hard":
  game(5) # 기회 5번 
else:
  print("Please enter 'easy' or 'hard'")
