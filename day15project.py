
profit = 0

def is_resource_sufficient(order_ingredients):
  is_enough = True
  for item in order_ingredients: # item (water, coffee, milk)
    if order_ingredients[item] > resources[item]: # 3개중 재료 하나라도 만족하지 못하면 false 반환 
      print(f"sorry there is not enough {item}.")
      is_enough = False # if 구문 활성화 안되면 is_enough는 계속 True
  return is_enough

def process_coins():
  """Returns the total calculated from coins inserted."""
  print("Please insert coins.")
  total = int(input("how many quarters?: ")) * 0.25 
  total += int(input("how many dimes?: ")) * 0.1
  total += int(input("how many nickles?: ")) * 0.05
  total += int(input("how many pennies?: ")) * 0.01
  return total # 합 반환 

def is_transaction_successful(money_received, drink_cost):
  """Return True when the payment is accepted, or False if money is insuffcient."""
  if money_received >= drink_cost:
    change = round(money_received - drink_cost,2) 
    print(f"Here is ${change} in change")
    global profit
    profit += drink_cost
    return True
  else:
    print("Sorry that's not enough money. Money refunded.")
    return False

def make_coffee(drink_name,order_ingredients):
  """Deduct the required ingredients from the resources"""
  for item in order_ingredients: # item (water, coffee, milk)
    resources[item] -= order_ingredients[item] # resources[item] 은 어느 함수에서 접근 가능  
  print(f"Here is your {drink_name}")

is_on = True 

while is_on: # 무한루프 
  choice = input("What would you like? (espresso/latte/cappuccino): ") # 커피 종류 입력 
  if choice == "off": # off 누를경우 반복 종료 
    is_on = False
  elif choice == "report": # report 입력시 커피 재료 출력 
    print(f"Water : {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money : ${profit}")
  elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
    drink = MENU[choice] # drink는 딕셔너리 
    if is_resource_sufficient(drink["ingredients"]): # drink["ingredient"]는 딕셔너리 , 먼저 커피 자판기에 재료가 충족되는지 확인 
      payment = process_coins() # 재료가 만족되면 가격 함수를 호출 
      if is_transaction_successful(payment,drink["cost"]): # 커피가격과 지불 가격을 비교하는 함수 호출 
        make_coffee(choice,drink["ingredients"]) # 커피를 만든다 + 재료를 삭감한다 
  else: # 오타 발생시 반복 종료 
    print("Please enter the coffee name (espresso/latte/cappuccino) ")
    is_on = False
