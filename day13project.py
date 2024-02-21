# debugging 

# 1. describe the problem (머릿속에서 문제 그려보기) 
# 2. Reproduce the bug (버그 재현)
# 3. Play Computer (컴퓨터 입장에서 생각해보기)
# 4. Fix the Errors (오류 수정하기)
# 5. Print is Your Friend (프린트 함수는 너의 친구)
# 6. Use a Debugger (디버거를 활용하자)
# 7. Take a Break 
# 8. Ask a Friend 
# 9. Run Often (단계마다 실행)
# 10. Ask Stackoverflow (스택오버플로우 질문)

for number in range(1,101):
  if number % 3 == 0 and number % 5 == 0:
    print("fizzbuzz")
  elif number % 3 == 0:
    print("fizz")
  elif number % 5 == 0:
    print("buzz")
  else:
    print(number)
