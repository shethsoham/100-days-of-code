#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
###

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


#Getting 4 random letters
random_letters=random.sample(letters, nr_letters)
a = ""
for let in random_letters  :
  
  a = let + "" + a

#Getting 2 random symbol
random_symbols=random.sample(symbols, nr_symbols)
b= ""
for sym in random_symbols  :
  b=sym+ "" +b

#Getting 2 numbers
random_numbers=random.sample(numbers, nr_numbers)
c=""
for num in random_numbers  :
  c = num+""+c


list_making = random_letters + random_numbers + random_symbols
random.shuffle(list_making)

d=""
for i in list_making :
  d=d+""+i
  #print(i, end="")
print(d)
