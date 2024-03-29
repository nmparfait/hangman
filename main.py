
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#TODO-4: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

from replit import clear
import random 
import hangman_words
chosen_word = random.choice(hangman_words.word_list)
lives = 6
from hangman_Art import logo, stages
print(logo)

display = []
word_length = len(chosen_word)

for _ in range(word_length):
  display += "_"

end_of_game = False

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  clear()

  if guess in display:
    print(f"You have already guessed {guess}")

  for position in range(word_length):
    letter = chosen_word[position]
    #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    if letter == guess:
      display[position] = letter

  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in te word. You lose a life.")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You lose.")

  print(display)

  if "_" not in display:
    end_of_game = True
    print("You win!")

  print(f'Pssst, the solution is {chosen_word}.')  
  print(stages[lives])








