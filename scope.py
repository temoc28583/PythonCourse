x= "hi" #variable like this is not local and can be used within functions

def greet():
    x="hello" #creating a var with same name with diff variable is local to this function only
    print(x)
def welcome():
    print(x)

def Global():
    global x
    x= "great"
    print(x)

#key function can be helpful to customize how to sort based on the value
greet()
welcome()
print(x)
Global()
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "mango"]
thislist.sort(key=str.lower, reverse=True) # or use reverse
print(thislist)
print(thislist[-4:-1]) #prints from -4 to -2
print(len(thislist))
thislist[1:3]= ["grapes", "papaya"] #length of this list will stay the same as we are not adding more items than replacing
print(len(thislist))
thislist[2:3]= ["blackcurrent", "rasberry", "orange"]
print(len(thislist)) #length changed by 2 we added teo additonal elements since the intention was to modify one element
i=0
while i<len(thislist):
    print(thislist[i])
    i=i+1


newList= [x for x in thislist]
print(newList)#way to do in one line of codde
acidList= [x for x in thislist if x=="banana" or x== "apple"] #added values to acidList based on if values from thislist
newList.append("banana")
print(newList.index("apple")) #prints index of  apples or the first index in which the list if first accessed
print(newList.count("banana")) #prints number of occurances of banana
newList.extend(acidList)#way to combine two lists
#ways to make copies of list
empList= newList.copy()
tempList= list(newList)
spliceList=newList[:]
rangeList= [x for x in newList]
arrList=[]
for x in newList:
    arrList.append(x)
