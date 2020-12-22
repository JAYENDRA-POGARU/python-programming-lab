class matrix:
    def __init__(self,List):
        self.List=List
    def disp(self):
        print(self.List)
    def __add__(self,M):
        temp=matrix([])
        print(len(self.List))
        for i in range(len(self.List)):
            for j in range(len(self.List[0])):
                temp.List.append(self.List[i][j]+M.List[i][j])
            return temp
M1=matrix([[1,2],[3,4]])
M2=matrix([[3,4],[5,1]])
M3=matrix([])
M3=M1+M2
M3.disp()
        
