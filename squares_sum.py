def sq(x):
    return x*x
s=list(map(sq,range(1,11)))
print(s)
sum=0
for i in s:
    sum+=i
print(sum)
