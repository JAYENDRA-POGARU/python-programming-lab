class student:
    def __init__(self):
        self.name=input("enter the name: ")
        self.roll=int(input("enter the roll number: "))
        self.mark=[]
        self.total=0
    def marks(self):
        for j in range(3):
            x=int(input("enter the marks in subjects %d:"%(j+1)))
            self.mark.append(x)
            self.total+=x
    def disp(self):
        print(self.name,"having roll number",self.roll,"acquired",self.total,"\n")
n=int(input("how many students:"))
si=[]
for s in range(n):
    s=student()
    si.append(s)
    s.marks()
for i in range(n):
    si[i].disp()

