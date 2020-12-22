class Binary:
    number = []
    def set(self,bnum):
        self.number = bnum
    def display(self):
        print(self.number)
    def __add__(self, B):
        Temp = Binary()
        index = len(self.number)
        carry = []
        while len(Temp.number) != index:
            Temp.number.append(-1)
            carry.append(0)
        index -= 1
        while(index) >= 0:
            if self.number[index] == 0 and B.number[index] == 0:
                Temp.number[index] = 0 + int(carry[index])
            if self.number[index] == 0 and B.number[index] == 1:
                Temp.number[index] = 1 + int(carry[index])
            if self.number[index] == 1 and B.number[index] == 0:
                Temp.number[index] = 1 + int(carry[index])
            if self.number[index] == 1 and B.number[index] == 1:
                Temp.number[index] = 0 + int(carry[index])
                carry[index-1] = 1
            if Temp.number[index] == 2:
                Temp.number[index] = 0
                if(index-1)>=0:
                    carry[index-1] = 1
            index -= 1
        return Temp
B1 = Binary()
B1.set([1,1,0,1,1])
B2 = Binary()
B2.set([0,1,1,0,1])
B3 = B1 + B2
B3.display()
                
