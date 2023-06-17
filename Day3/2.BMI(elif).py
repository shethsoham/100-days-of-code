# if (Condition):
#     ....
#     ....
# elif (Condition):
#     ....
#     ....
# else :
#     ....
#     ....

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bMI = round(weight/height**2)
#bMI= round(bMI,2)
if (bMI < 18.5):
    print(f"Your BMI is {bMI}, you are underweight.")
elif (bMI > 18.5 and bMI < 25):
    print(f"Your BMI is {bMI}, you have a normal weight.")
elif (bMI > 25 and bMI < 30):
    print(f"Your BMI is {bMI}, you are slightly overweight.")
elif (bMI > 30 and bMI < 35):
    print(f"Your BMI is {bMI}, you are obese.")
else:
    print(f"Your BMI is {bMI}, you are clinically obese.")



