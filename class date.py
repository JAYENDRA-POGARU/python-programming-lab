Dict={1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
def chklp(yr):
    if((yr%4==0 and yr%100!=0) or (yr%400==0)):
        return 1
    else:
        return 0
class date:
    def __init__(self):
        d=m=y=0
    def get(self):
        self.d=int(input("Enter day:"))
        self.m=int(input("Enter month:"))
        self.y=int(input("Enter year:"))
    def __add__(self,num):
        self.d+=num
        if(self.m!=2):
            max=Dict[self.m]
        elif(self.m==2):
            isLeap=chklp(self.y)
            if(isLeap==1):
                max=29
            else:
                max=28
        while(self.d>max):
            self.d-=max
            self.m+=1
        while(self.m>12):
            self.m-=12
            self.y+=1
    def disp(self):
        print(self.d,"-",self.m,"-",self.y)
D=date()
D.get()
num=int(input())
D+num
D.disp()
        
        
