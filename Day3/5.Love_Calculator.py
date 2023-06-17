# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.upper()

name2 = name2.upper()


#truelove

T1 = name1.count("T")
R1=name1.count("R")
U1=name1.count("U")
E1=name1.count("E")
T2=name2.count("T")
U2=name2.count("R")
R2=name2.count("U")
E2=name2.count("E")

count_TRUE = T1+T2+R1+R2+U1+U2+E1+E2


L1 = name1.count("L")
O1 = name1.count("O")
V1 = name1.count("V")
E1 = name1.count("E")

L2 = name2.count("L")
O2 = name2.count("O")
V2 = name2.count("V")
E2 = name2.count("E")

count_LOVE = L1+L2+O1+O2+V1+V2+E1+E2



true_love = str(count_TRUE) + str(count_LOVE)
#true_love = int(true_love)

true_love1 = int (true_love)
if (true_love1 <= 10 or true_love1 >= 90 ):
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif (40 <= true_love1 and 50>= true_love1):
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")









