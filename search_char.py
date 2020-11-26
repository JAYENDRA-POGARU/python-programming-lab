str="Hello and welcome"
ch=input()
c=0
m=0
for i in str:
    if(ch==i):
        print("present at index ",c)
        m=1
    c=c+1
if(m==0):
    print("not present in string")
