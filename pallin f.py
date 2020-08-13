#3. Write a program to check whether the number is a palindrome or not using functions.
n=int(input("Enter number:"))
def findpalin(n):
    x=n
    rev=0
    while(n>0):
        d=n%10
        rev=rev*10+d
        n=n//10
    if(x==rev):
        print("The number is a palindrome.")
    else:
        print("The number isn't a palindrome.")
findpalin(n);
