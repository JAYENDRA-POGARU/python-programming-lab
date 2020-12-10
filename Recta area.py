class rect:
    def getdata(self):
        rect.length=int(input("enter the length:"))
        rect.breadth=int(input("enter the braedth:"))
    def showdata(self):
        print("length=",rect.length,"\tBreadth=",rect.breadth)
    def area(self):
        print("area=",rect.length*rect.breadth)

rec=rect()
rec.getdata()
rec.showdata()
rec.area()
