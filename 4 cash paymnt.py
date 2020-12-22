class Bill:
    def __init__(self,items,price):
        self.total=0;
        self.items=items
        self.price=price
        for i in self.price:
            self.total += i
    def display(self):
        print("\n ITEM \t\t\t PRICE")
        for i in range(len(self.items)):
            print(self.items[i], "\t", self.price[i])
        print("***************")
        print("TOTAL= " , self.total)
class Cash_payment(Bill):
    def __init__(self,items,price,deno,value):
        Bill.__init__(self,items,price)
        self.deno=deno
        self.value= value
    def show_Cash_payment_Details(self):
        Bill.display(self)
        for i in range(len(deno)):
            print(deno[i],"*",value[i],"=",deno[i]*value[i])
class Cheque_payment(Bill):
    def __init__(self,items,price,cno,name):
        Bill.__init__(self,items,price)
        self.cno=cno
        self.name=name
    def show_Cheque_payment_Details(self):
        Bill.display(self)
        print("cheque number : ",self.cno)
        print("bank name : ",self.name)
items = ["external hard disk","ram","printer","pen drive"]
price = [5000,2000,6000,3000]
option = int(input("would you like to pay by cheue or cash (1/2):"))
if(option==1):
    name = input("enter the name of the bank:")
    cno = input("enter the cheque number:")
    Cheque = Cheque_payment(items,price,cno,name)
    Cheque.show_Cheque_payment_Details()
else:
    deno = [10,20,50,100,500,2000]
    value = [1,1,1,20,4,5]
    CP = Cash_payment(items,price,deno,value)
    CP.show_Cash_payment_Details()
        
        
        

