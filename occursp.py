str="Hello and welcome"
print(str)
ch=input()
n=int(input())
c=0
str=str+'n'
for i in range(n,len(str)):
    if(ch==str[i]):
        c=c+1
print(c)
