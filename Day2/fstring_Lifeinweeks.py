# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#age_ninty = 90 year , 4680 weeks, 32850 days, 1080 months

days =(32850-int(age)*365)
weeks = (4680-int(age)*52)
months = (1080-int(age)*12)

print(f"You have {days} days, {weeks} weeks, and {months} months left." )

