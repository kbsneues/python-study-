# 딜러에게 카드를 한장씩 받아 21에 가까운 수를 만드는 사람이 승리 
# 카드의 합이 21점 또는 21을 초과하면 지는 게임 
# 딜러는 가진 카드의 합계가 16점 이하이면 반드시 1장을 더 받아야 함 
# 딜러는 17점 이상이면 카드를 더 받지 않고 멈춘다 

import random 
from art import logo
from replit import clear


def deal_card(): # 카드를 무작위로 뽑아 반환하는 함수 
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards) 
  return card 

def calculate_score(cards): # 리스트에 있는 카드의 합을 반환하는 함수 
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and len(cards) == 2: # 카드가 10 11 일 때 종료 
    return 0

  if 11 in cards and sum(cards) > 21: # 카드가 11이고 합이 21 넘을 때 11을 1로 바꾼다 
    cards.remove(11)
    cards.append(1)
  
  return sum(cards)

def compare(user_score, computer_score): # 유저와 컴퓨터의 값을 비교하는 함수 
  if user_score == computer_score: # 값이 같을 때 
    return "Draw"
  elif computer_score == 0: 
    return "Lose, opponent has blackjack"
  elif user_score == 0:
    return "Win with a blackjack"
  elif user_score > 21: 
    return "you went over. you lose"
  elif computer_score > 21:
    return "opponent went over. you win"
  elif user_score > computer_score: # user_score, computer_score 모두 21점을 넘지 않는다, 순서를 고려하자 
    return "you win"
  else:
    return "you lose"
  


def play_game(): # 게임 시작 
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2): # 2번 반복, 처음 유저, 컴퓨터의 카드가 2개를 지급받는다 
    user_cards.append(deal_card()) # 하나의 항목만을 추가하려면 append 사용   
    computer_cards.append(deal_card()) 
  
  while not is_game_over: # 무한루프 
    
    user_score = calculate_score(user_cards) # 유저가 가지고 있는 카드의 합 
    computer_score = calculate_score(computer_cards) # 컴퓨터가 가지고 있는 카드의 합 
    print(f"    Your cards: {user_cards}, current score: {user_score}")
    print(f"    Computer's first card : {computer_cards[0]}") # 컴퓨터가 가지고 있는 첫번째 카드 
    
    if user_score == 0 or computer_score == 0 or user_score > 21: # 유저 카드의 합이 21점 넘거나 0점 이거나 , 컴퓨터 카드의 합이 0점 일 때 반복을 종료 
      is_game_over = True
    else: # 유저 카드, 컴퓨터 카드 의 합이 21점 넘지 않을 때 
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ") # 카드를 더 받을 것인가? 
      if user_should_deal == "y":
        user_cards.append(deal_card()) # 카드 1개를 지급 받는다  
      else:
        is_game_over = True # 반복을 종료 
  
  while computer_score != 0 and computer_score < 17: # 컴퓨터 카드의 합이 0이 아니고 17미만 일 경우 
    computer_cards.append(deal_card()) # 카드를 1개 지급 받는다 
    computer_score = calculate_score(computer_cards) # 총합을 저장 
  
    print(f"    your final hand: {user_cards}, final score: {user_score}")
    print(f"    computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score)) # compare 함수를 호출하여 두 값을 비교한다 
    
while input("Do you want to play a game of blackjack type 'y' or 'n' ") == 'y': # 게임을 시작하고 싶은지 묻는다 
  clear() 
  play_game() # 게임 시작 
