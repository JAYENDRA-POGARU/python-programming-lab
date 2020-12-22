class Distance:
    def __init__(self):
        self.km = 0
        self.m = 0
    def set(self, km, m):
        self.km = km
        self.m = m
    def __isub__(self, D):
        self.m = self.m - D.m
        if self.m < 0:
            self.m += 1000
            self.km -= 1
        self.km = self.km - D.km
        return self
    def convert_to_meters(self):
        return (self.km*1000 + self.m)
    def display(self):
        print(self.km, "kms" , self.m , " mtrs" )
D1 = Distance()
D1.set(21,70)
D2 = Distance()
D2.set(18,123)
D1 -= D2
print(" D1-D2 = ")
D1.display()
print("That is " , D1.convert_to_meters(),"meters")
