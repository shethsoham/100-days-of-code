# Minimum number in an array
array = [123, 23 , 45,450, 67 ,32, 322 ,10, 5 , 2, 76 ]

min_number = 1000000000000000000000000000000000000000000

for i in array:
    if i < min_number:
        min_number = i

print(min_number)