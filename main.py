word_list = ["paradis", "python", "parfait"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

import random 
chosen_word = random.choice(word_list)


#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

#Testing code
print(f'Pssst, the solution is {chosen_word}.') 

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
display = []
word_length = len(chosen_word)

for _ in range(word_length):
  display += "_"

for position in range(word_length):
  letter = chosen_word[position]
   #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
  if letter == guess:
    display[position] = letter

print(display)

#Testing code


#TODO-4: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.


