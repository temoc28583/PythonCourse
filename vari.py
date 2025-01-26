#this is a commenrt line
#use hashmark

name= "Rashi"#statement we are assigning a string to a variable
age=75 #we can create variables consiting of characters,numbers,etc
my_name= "John"#can use underscore
#name2#Cannot declare variable blank
#unacceptable: 1name test! or test%
#statement:operation on a value
print(name);print(age)#use mutliple statements on one line
#data types
ageOne=17 #this is an integer
print(type(ageOne))#print the type of the data type <class'int'>
print(type(ageOne)== int) #can be used as a comparison: 
print(isinstance(ageOne,int)) #used to see if a variable is an instance of ageOne
print(isinstance(2,float)) #prints false for this to return true, we can make it into a float via a class constructot
newNum= float(2)
print(isinstance(newNum,float))#prints true
#conversion of data type(string to int)

numOne= int("20")#refered to casting
print(isinstance(numOne,int)) #prints true 
origOne= int(numOne)
print(isinstance(origOne,int))
a=b=c = "Orange"
d,e,f= "Hi", "Hello", "world"
print(a,b,c)
print(d,e,f)
numbers=[1,2,3]
numOne,numTwo,numThree= numbers #reffered to as unpacking where we can assign values from alist,tuple to variables
print(numOne)
print(numTwo)
print(numThree)

