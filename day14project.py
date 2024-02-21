import random 

from replit import clear
from art import logo,vs
from game_data import data # data는 총 50개, 배열 인덱스 0~49 

score = 0

def make(): # 랜덤 숫자 반환 
  global data
  return random.randrange(len(data))

def inform(number): # 해당 정보 출력
  global data 
  return (f'{data[number]["name"]}, {data[number]["description"]}, from {data[number]["country"]}')

def follower(number): # 팔로워 수 반환 
  global data
  return data[number]["follower_count"]

def start_game(compare_a, against_b): # 2명의 정보를 출력
  print(f"Compare A : {inform(compare_a)}")
  print(vs)
  print(f"Against B : {inform(against_b)}")

def compare(compare_a, against_b, select): # 팔로워 수를 비교 , 점수를 출력 
  global score
  if follower(compare_a) > follower(against_b) and select == "a":
    score += 1 
    print(f"You're right! Current score : {score}")
  elif follower(compare_a) < follower(against_b) and select == "b":
    score += 1 
    print(f"You're right! Current score : {score}")
  else:
    print(f"Sorry, that's wrong. final score : {score}")
    return 0

def game():
  while True:
    compare_a = make() # 0~49 까지의 임의의 정수
    against_b = make() # 0~49 까지의 임의의 정수 
  
    print(logo)
    start_game(compare_a, against_b)
  
    select = input("Who has more followers? Type 'A' or 'B': ").lower()
    clear()
    
    if compare(compare_a,against_b,select) == 0:
      break


game() 


# ------------------------------


from art import logo,vs 
print(logo)

from game_data import data 

import random 
from replit import clear

def format_data(account): # 딕셔너리를 받아서 각 정보에 접근 
  """Format the account data into printable foramt """
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}" # 문자열 반환 
  
def check_answer(guess,a_followers,b_followers):
  """Use if statement to check if user is correct."""
  if a_followers > b_followers: 
    return guess == "a" # True or false , 더 간결한 방법 
  else:
    return guess == "b"


score = 0
game_should_continue = True

account_b = random.choice(data) # acoount_b는 딕셔너리 


while game_should_continue: # 무한루프 
  
  account_a = account_b
  account_b = random.choice(data)

  while account_a == account_b: # a와 b가 같을 때 
    account_b = random.choice(data) # 다시 랜덤함수 사용 
    
  print(f"Compare A : {format_data(account_a)}")
  print(vs)
  print(f"Against B : {format_data(account_b)}")
  
  guess = input("who has more followers? a or b? ").lower()
  
  
  a_follower_count = account_a["follower_count"] # a의 팔로워수 저장 
  b_follower_count = account_b["follower_count"]
  
  is_correct = check_answer(guess,a_follower_count,b_follower_count) # 결과 출력 

  clear()
  print(logo)
  
  if is_correct:
    score += 1 
    print(f"you're right! current score : {score}")
  else:
    game_should_continue = False # 무한 루프 종료 
    print(f"sorry,that's wrong. final score : {score}")

  
