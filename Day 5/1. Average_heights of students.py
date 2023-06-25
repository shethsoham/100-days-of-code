#average height of students 

sum = 0 
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  print(student_heights[n])
  sum = sum + student_heights[n]

total = n + 1 

print(sum)
print(total)
avg = sum / total 

print (avg)