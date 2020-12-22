class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def disp(self):
        print(self.name,self.marks)
    def __add__(self,S):
        temp=student(S.name,[])
        for i in range(len(self.marks)):
            temp.marks.append(self.marks[i]+S.marks[i])
        return temp
s1=student("jay",[99,96,99])
s2=student("chai",[99,95,99])
s1.disp()
s2.disp()
s3=student(" ",[])
s3=s2+s1
s3.disp()

            
