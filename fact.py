#2.Python program to find factorial of number

n=int(input("Enter the number : "))
f=1
if n<0:
    print("not possible")
else:
    for i in range(1,n+1):
        f=f*i
    print("factorial of given number is",f)
