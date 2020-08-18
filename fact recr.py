def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)

n=int(input("Enter number"))
f=fact(n)
print("factorial of ",n,"is ",f)
