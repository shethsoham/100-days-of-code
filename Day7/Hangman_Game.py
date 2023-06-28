# 6 lives 
'''
1) what if it is present 2 times 
2) same option selected twice 
3) fill it in a variable and lastly fill it out 
4) make sure about the sequence 
5) lives contidion n for loop


'''




import random # Importing random variable 
words = ['Apple', 'Mobile', 'Indians'] # Created a imaginary array of 3 words
word = random.choice(words) # used random method and choosed 1 word from array
word = word.lower() # lower cased all the words which would get selected 
print(word) # After you have finally build the game delete this statement should not be visible to the player 

lives = 6  # this is by default set there will be only 6 lives and you can first write the print statements 
           # you can write the rule 
for i in range (0, lives):
    guess_Character = input("Enter the character user wants to guess ")
    if guess_Character in word :
        print ("Right")
        print("lives left",lives) # same number of lives will stat for every correct answer
    else: 
        print("wrong")
        lives = lives - 1  # for every wrong choice you will loose one live in total you have 6 lives 
        print("lives left",lives)
        if lives == 0 :
            print("Sorry You lost the game , want to try again ?")

