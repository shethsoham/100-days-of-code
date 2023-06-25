## Choose randomly who will be paying the bills

# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆


length = len(names)
lenght = length - 1
random_number = random.randint(0,length)

print(names[random_number] + " is going to buy the meal today!")

# input 
#Angela, Ben, Jenny, Michael, Chloe

#Write your code below this line 👇
