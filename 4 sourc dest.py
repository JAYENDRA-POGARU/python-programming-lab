class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def get(self):
        return(self.x,self.y)
class Location:
    def __init__(self,x1,y1,x2,y2):
        self.source=point(x1,y1)
        self.destination = point(x2,y2)
    def show(self):
        print("Source = ",self.source.get())
        print("Destination = ",self.destination.get())
    def reflection(self):
        self.destination.x =- self.destination.x
        print("Reflection Point on x axis is:",self.destination.x,self.destination.y)
L = Location(1,2,3,4)
L.show()
L.reflection()

