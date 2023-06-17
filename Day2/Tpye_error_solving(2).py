#type error
#type casting 

num_char = len(input("What is your name ?"))
#print("Yourn name has"+ num_char + "characters.")

new_num_char = str(num_char)
# type error can only concatenate str (Not "int") to str

# How to see which data tpe you are working with ?
print("Yourn name has"+ new_num_char + "characters.") 
# All data dtypes are string here 
print(type(num_char))
print(type(new_num_char))
