

#1. Create a greeting for your program.
print("hello world")
#2. Ask the user for the city that they grew up in.
city_name = input("where did you grow up ?\n")
print(city_name)
#3. Ask the user for the name of a pet.
pet_name = input("enter your pet name\n")
print(pet_name)
#4. Combine the name of their city and pet and show them their band name.
print(city_name + pet_name )
#5. Make sure the input cursor shows on a new line:
# Solution: https://replit.com/@appbrewery/band-name-generator-endsoham

'''
10 June 2024
'''


print("Hello welcome the project named band name generator")
user_city = input("What is the name of the city you grew up in?\n")
user_pet = input("What is the name of your pet?\n")
band_name = user_city + ""+ user_pet
print("your band name is ",band_name)