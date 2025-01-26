
import random
thislist=[1,2,3,4,5,6,7,8,9,10]
nameList= ["Abby", "Kayla", "Rashi", "Rishi"]

for x in nameList:
    if "A" in x or "R" in x :
        print(x)


print("Kayla" in nameList)

evenList=[num for num in thislist if num%2==0] 
i=0
while i<len(evenList):
    print(evenList[i])
    i=i+1



print(thislist[-4:-1])#print 7,8,9 since -1 refers to the last element(work to the left)
print(nameList[random.randrange(0, len(nameList))])
