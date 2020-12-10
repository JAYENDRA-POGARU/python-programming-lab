class Stud:
    def __init__(self,name):
        self.name=name
        self.marks=[]
    def entermarks(self):
        for i in range(3):
            m=int(input("Enter marks of %s in subject %d :"%(self.name,i+1)))
            self.marks.append(m)
    def display(self):
        print(self.name, "got",self.marks)

s1=Stud("Jay")
s1.entermarks()
s2=Stud("Chai")
s2.entermarks()
s1.display()
s2.display()
