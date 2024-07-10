#Hangman step by step
import random
from hangman_words import word_list
random_word = random.choice(word_list)
#guess_letter = input("Guess the letter").lower()

length = len(random_word)

initial_list = []
for i in range(0,length):
    initial_list.append("_")
    
print(initial_list)

end_of_game = False
lives = 6
while not end_of_game:
    guess_letter = input("Guess the letter ").lower()
   
    for single_letter in range(0,length):
        if guess_letter == random_word[single_letter]:
            initial_list[single_letter] =  guess_letter
        
    print(initial_list)

    if guess_letter != random_word[single_letter]:
        lives = lives - 1
        if lives == 0:
            end_of_game = True
            print("You loose")
            print("Random guessed word was ",random_word)
    if "_" not in initial_list:
        end_of_game = True
        print("You won")
        print("Random guessed word was ",random_word)

    
    
