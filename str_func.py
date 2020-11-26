def check(x):
    if(x%2==0 or x%4==0):
        return 1 
evens=list(filter(check,range(2,22)))
print(evens)

def add2(x):
    x+=2
    return x
num=[1,2,3,4,5,6,7,8,9]
print(num)
new=list(map(add2,num))
print(new)


def ad(x,y):
    return x+y
l=[1,2,3,4]
r=[5,6,7,8]
lr=list(map(ad,l,r))
print(lr)

import functools
def add(x,y):
    return x+y
l=[1,2,3,4,5,6]
print(functools.reduce(add,l))
