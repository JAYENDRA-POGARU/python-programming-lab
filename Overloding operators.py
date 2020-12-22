#5.Write a program that overloads the *,/ and > operator so that can multiply, divide and compare two objects of class Fraction.
def GCD(num,deno):
    if(deno==0):
        return num
    else:
        return GCD(deno, num%deno)
class Fraction:
    x=y=0
    def __init__(self):
        self.num=0
        self.deno=1
    def get(self):
        self.num=int(input("Enter the numerator: "))
        self.deno=int(input("Enter the denominator: "))
    def simplify(self):
        common_divisor=GCD(self.num,self.deno)
        self.num//=common_divisor
        self.deno//=common_divisor
    def __gt__(self,F):
        Flag = False
        self.x=self.num/self.deno
        self.y=F.num/F.deno
        if self.x > self.y:
            Flag=True
        return Flag
    def __mul__(self,C):
        temp=Fraction()
        temp.num= self.num*C.num
        temp.deno= self.deno*C.deno
        return temp
    def __truediv__(self,D):
        temp1=Fraction()
        temp1.num=self.num*D.deno
        temp1.deno=self.deno*D.num
        return temp1
    def display(self):
        self.simplify()
        print("\t   ",self.num,"/",self.deno)
F1=Fraction()
F1.get()
F2=Fraction()
F2.get()
print("F1 > F2",F1>F2)
F3=F1*F2
print("F1 * F2 IS : ")
F3.display()
F4=F1/F2
print("F1 / F2 IS : ")
F4.display()
