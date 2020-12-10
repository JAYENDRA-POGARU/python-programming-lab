class circle:
    Pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return circle.Pi*self.radius*self.radius
    def circumference(self):
        return 2*circle.Pi*self.radius
r=int(input("enter radius of circle:"))
c=circle(r)
print("area= ",c.area())
print("circumference= ",c.circumference())

        
