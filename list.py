import random
fruit=["apples","bananas","cherries",5,True] #can store various types of data
print(random.choice(fruit))#prints random value from the list
print("apples" in fruit) #way to check if item in a list
print(fruit[1])
fruit[1]= "oranges"
print(fruit[1])
print(fruit[-1]) #prints true, as negative index starts from the end so -1 will start from True
print(fruit[1:4])#reffered to as slicing, prints elements from 1 to 3(not including 4)
print(fruit[:3])#prints apples,oranges,cherries
print(len(fruit))
fruit.append("Water") #way to add item to list
empList=[]
fruit.extend(empList)
for x in range(len(fruit)):
    print(fruit[x])
fruit+=[1,2]
fruit.remove("Water")
print(fruit.pop()) #pops last element and prints it
print(fruit.pop(2))#pops the second element and return it
print(fruit)

fruit[1:1]=["Hi","Hello"] #assign multiple values by slicing
print(fruit[1:3])
name=["John", "bob"]
name.sort(key=str.lower)#prints string in alpha order regardless of upper or lower case
print(name)
sortList= name.sort(key=str.lower)
#print(sortList)
print(fruit)
print(fruit[3:]) #prints everything from index 3 to the end
print(random.choice(name)) #prints a random name from the names list
name.append("Oliver")
print(name[2])