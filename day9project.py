from replit import clear
from art import logo
print(logo)


all_data = [] # 빈 배열 

kbs_program = True


def best_bid(auction_data):
  max = auction_data[0]["bid"] # 첫번째 사람 bid
   
  for i in auction_data:
    if max < i["bid"]: # 모든 사람 bid 값 비교 
      max = i["bid"]
      best_name = i["name"]
  
  print(f"The winner is {best_name} with a bid of {max}")


while kbs_program: # 무한 루프 
  
  name = input("What is your name? :  ")
  bid =  int(input("What's your bid? : "))

  auction_dic = {} # 각 사람의 정보 저장 
  auction_dic["name"] = name
  auction_dic["bid"] = bid
  all_data.append(auction_dic) # 빈 배열에 추가 
  
  ask_question = input("Are there any other bidders? Type 'yes' or 'no'\n")

  if ask_question == "no": # 다른 이름이 없을 떄 
    kbs_program = False # while 반복문 종료 
  elif ask_question == "yes":
    clear()
    
best_bid(all_data) 

  
# ---------------------------------------------
# 상대방 

from replit import clear
from art import logo 

print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record): # bidding_record는 딕셔너리 
  highest_bid = 0
  winner = ""
  
  for bidder in bidding_record:               # bidder         bidder 
    big_amount = bidding_record[bidder] # bidding_record = {"Angela": 123, "James": 321}
    
    if big_amount > highest_bid:
      highest_bid = big_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")    

      
while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $")) # 숫자이므로 int형으로 변환
  bids[name] = price # {"Angela": 123} "Angela"는 key   123은 value
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")

  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
    

