def gcd(num,deno):
    if(deno==0):
        return num
    else:
        return gcd(deno,num%deno)
class fract:
    def __init__(self):
        self.num=0
        self.deno=1
    def get(self):
        self.num=int(input("enter the nume:"))
        self.deno=int(input("enter the deno:"))
    def simplify(self):
        cd=gcd(self.num,self.deno)
        self.num//=cd
        self.deno//=cd
    def __add__(self,F):
        temp=fract()
        temp.num=(self.num*F.deno)+(F.num*self.deno)
        temp.deno=self.deno*F.deno
        return temp
    def disp(self):
        self.simplify()
        print(self.num,"/",self.deno)
F1=fract()
F1.get()
F2=fract()
F2.get()
F3=fract()
F3=F1+F2
F3.disp()
            
