import random
print("Hello", "World")
print("Hellp"+"World")
print("hi",5) #to print variables with diff data types, use comma
x=5
#comp=8+j#known as a complex number
print(float(x))#can convert int to float,prints 5.0
print(complex(x)) #prints 5+0j
y=9.0
print(int(y))
print(complex(y))#int and float can be conferted into each other and each can be converted into complex but complxes cannot be converted into either

numbers=[1,2,3,4,5,6]
print(numbers.pop(random.randrange(0,len(numbers))))#prints and removes a number from a random index from 0 to the size of the list
w= float("28") #prints 28.0
z= float("34.5") #prints 34.5
print(w,z)

#error, due to the decimal d=int("39.8")
d= int("8")
print(d)

f=str(98.0)
g=str(9)
print(f,g)
intNum=int(98.75)
print(intNum) #truncates to 98