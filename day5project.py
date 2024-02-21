import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

alphabet_arry = [] # 알파벳 담는 배열 
for i in range(0,nr_letters): # 알파벳 개수 
  alphabet_number = random.randint(0,len(letters)-1) 
  alphabet_arry.append(letters[alphabet_number])

numbers_arry = [] # 숫자 담는 배열 
for i in range(0,nr_numbers):
  numbers_number = random.randint(0,len(numbers)-1)
  numbers_arry.append(numbers[numbers_number])

symbols_arry = [] # 특수기호 담는 배열 
for i in range(0,nr_symbols):
  symbols_number = random.randint(0,len(symbols)-1)
  symbols_arry.append(symbols[symbols_number])

result_password = ''.join(alphabet_arry) + ''.join(numbers_arry) + ''.join(symbols_arry) # result_password는 문자열
print(f"차례대로 배열한 비밀번호 {result_password}")

retry_arry = [] # 새로 재배열한 비밀번호 담는 배열 

while int(len(retry_arry)) != int(len(result_password)): # result_password의 길이만큼 반복 
  retry_number = random.randint(0,len(result_password)-1) # 계속해서 난수를 생성한다 
  if result_password[retry_number] not in retry_arry: # 해당 기호가 배열안에 있는지 묻는다 
    retry_arry.append(result_password[retry_number]) # 만약 없으면 해당 배열에 문자를 추가한다 

retry_password = ''.join(retry_arry) # retry_password는 문자열 
print(f"재배열한 비밀번호 {retry_password}")


# choice 함수 적용 
# range 함수 구간 변경 
# randint를 사용하지 않았음 
# shuffle 함수를 사용해서 배열을 임의적으로 재배열 할수 있다 
