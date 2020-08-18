a=int(input("enter upper range:"))
b=int(input("enter lower range:"))

def arms(n):
      sum=0
      temp=n
      while temp>0:
             d=temp%10
             sum+=d*d*d
             temp//=10
      if n==sum:
          print(n)


for i in range(a,b+1):
      arms(i)
