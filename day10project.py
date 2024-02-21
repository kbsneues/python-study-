# def my_function():
# return # 리턴 키워드 

# # 독스트링은 함수 시작 부분에서 함수 인터페이스를 설명하는 문자열이다 
# 관례상 모든 독스트링은 삼중 따옴표 문자열을 쓰며, 큰따옴표 3개를 쓰면 문자열을 두 줄 이상 쓸 수 있어서 긴 줄 문자열이라고 한다 
# 함수가 무엇을 하는지 간결하게 설명되어야 함 


# calculator 

from art import logo
from replit import clear

def add(n1,n2):
  return n1 + n2 

def substract(n1,n2):
  return n1 - n2 

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1 / n2 

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}

def calculator():
  
  num1 = float(input("What's the first number?: "))
  
  for symbol in operations:
    print(symbol)
  
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation : ")
    num2 = float(input("What's the next number? : "))
    
    calculation_function = operations[operation_symbol] 
    # 함수이름 (add, substract, multiply, divide)
    
    answer = calculation_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    
    if  input("Type 'y' to continue calculating with 8, or type 'n' to exit. : ") == 'y': 
      num1 = answer # 해답을 num1에 저장하고 num2는 계속해서 입력받는다 
    else:
      should_continue = False
      clear()
      calculator() # 첫번째 숫자부터 입력받는다 (재귀) 

calculator()
