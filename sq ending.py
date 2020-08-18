a=0
b=0
for i in range(1,100):
    n=i*i
    m=n%10
    if(m==4):
        a=a+1
    elif(m==9):
        b=b+1

print("Number of squares ending in 4 are ",a)
print("Number of squares ending in 9 are ",b)
