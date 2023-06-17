#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to Tip calculator")
bill = float(input("What was the total bill  ?$"))
tip = int(input("How much percent tip will you like to give ?"))
people = int(input("Within how many people you want to split ?"))
tip_as_percentage = tip/100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill/people
final_amount = round(bill_per_person,2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each Person should pay : ${final_amount}")
