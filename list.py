#list
numlist=[1,2,3,4,5,6,7,8,9,10]
print("number list is: ",numlist)
print("First element in list is: ",numlist[0])
print("numlist[2:5]= ",numlist[2:5])
print("numlist[ : :2]= ",numlist[ ::2])
print("numlit[1::3]= ",numlist[1::3])
numlist.append(10)
print(numlist)
del numlist[3]
print(numlist)
