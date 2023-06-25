#Python List 

#List is a datastructure , List is a array. 

# Variable is also a data structure where it is just storing a one piece of number or character 
#a = 3

# List is pretty aimple its just a set of square brackets with item stored 
# inside thode items can be of any datatype or can have mixed data tyype
#fruit= [item1,item2]
#fruits = ["Apple","Orange","Cherry"]

#if we don't know list data structure the we would have denoted it like
# state1 = michigan
# state2 = Delaware
#But now as we know the list data structure ir is quite simple to write all 50 states toghether using 1 name  
# states_of_america = ["michigan","Delaware","Pensalvenia"]
# print(states_of_america[0])

states_of_america = ["michigan", "Delaware", "Pennsylvania"]

# Understanding the positions 
print(states_of_america[0])
print(states_of_america[-1])

#Appending the list
states_of_america.append("India")
print(states_of_america)

#Extending the lists
states_of_america.extend(["Mumbai","pune","siattle","washington"])
print(states_of_america)
