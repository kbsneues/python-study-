import random 

from hangman_words import word_list 

chosen_word = random.choice(word_list) 
word_length = len(chosen_word)

end_of_game = False
lives = 6 

from hangman_art import logo,stages
print(logo)

print(f"Psset, the solution is {chosen_word}.")

display = [] # 단어를 저장하는 배열 생성 

for _ in range(word_length):
  display += "_" # 배열이기때매 + 사용가능

while not end_of_game: # 무한루프
  guess = input("Guess a letter : ").lower()

  if guess in display: # 단어가 배열에 있으면 
    print(f"You've already guessed {guess}")

  for position in range(word_length): # 선택된 단어 
    letter = chosen_word[position] 
    if letter == guess: 
      display[position] = letter

  if guess not in chosen_word: # guess : 문자 , chosen_word : 문자열 
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives -= 1
    if lives == 0: # lives가 0이 되는 구역이 단어 가 없을때 임 
      end_of_game = True
      print("You lose.")
  print(f"{' '.join(display)}")

  if "_" not in display: # "_" 단어가 배열에 없을 때 게임을 종료 
    end_of_game = True
    print("You win.")

  print(stages[lives])
