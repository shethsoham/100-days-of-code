#

#def key word 
#() --> parenthesis

def greet ():
    print("Hello let learn fast")
    print("Let's Go for day 9")
    print("Go step b step")

print("Down we will see all 3 statements printed")
greet()

#function which allows the input

def greet_with_name(name):
    print(f"Hello ")
    print(f"Hello do you do {name}")

greet_with_name("Soham")

'''
Here 
name is parameter (variable)
and 
Soham is the argument (value)
'''

# Functions with multiple inputs 

'''
So for example take a array and give multiple value in that 


'''

#More then 1 parameters 

def greet_with(name, location):

    print(f"Hello {name}")
    print(f"What it is like in {location}")

print("Functions with multiple inputs or parameters")
greet_with("Soham", "Michigan" )

#Positional Inputs : Position of the function matters

def positional_argument(a,b,c):
    print("Value of a is ",a)
    print("Value of b is ",b)
    print("Value of c is ",c)
positional_argument(1,2,3)
positional_argument(3,2,1)
#Now here value of a, b and c has been changed 
#------------------------------------------------------------------------------#
#Keyword arguments : postion of the function does not matters 

def keyword_argument(a,b,c):
    print("Value of a is ",a)
    print("Value of b is ",b)
    print("Value of c is ",c)
keyword_argument(a=1,b=2,c=3)
keyword_argument(c=3,b=2,a=1)

#Here the value of parameters is not changed
