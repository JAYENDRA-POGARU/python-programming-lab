#4.Program to check whether a string is pallindrome or not

str=input("Enter a string:")

for i in range(0,int(len(str)/2)):
    if str[i]!=str[len(str)-i-1]:
        x=0
    else:
        x=1

if(x):
    print("pallindrome")
else:
    print("not a pallindrome")
   
