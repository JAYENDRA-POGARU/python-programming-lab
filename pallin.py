#3.Python program to check whether a number is pallindrome or not

n=int(input("Enter a number : "))

r=0
temp=n
while(n>0):
    x=n%10
    r=r*10+x
    n=n//10
if(temp==r):
    print("The number is a pallindrome")
else:
    print("The number is not a pallindrome")
