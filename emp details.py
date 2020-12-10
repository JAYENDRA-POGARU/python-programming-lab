class emp:
    empcount=0
    def __init__(self,name,desig,salary):
        self.name=name
        self.desig=desig
        self.salary=salary
        emp.empcount+=1
    def displaycount(self):
        print("there are %d employees"%emp.empcount)
    def displaydetails(self):
        print("name:",self.name,"\ndesignation:",self.desig,"\nSalary:",self.salary)

e1=emp("Jay","Manager",10000)
e2=emp("Chai","team lader",90000)
e3=emp("ram","Programmer",80000)
e4=emp("RAjUY","officer",60000)
e4.displaycount()
e2.displaydetails()
