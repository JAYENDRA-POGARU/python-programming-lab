

n=int(input("enter number"))
sum=0
temp=n
while temp>0:
    d=temp%10
    sum+=d*d*d
    temp//=10
if n==sum:
    print("armstrong")
else:
    print("not armstrong")
