class store:
    __item_code = []
    __price = []

    def get_data(self):
        for i in range(5):
            self.__item_code.append(int(input("Enter the code of item : ")))
            self.__price.append(int(input("Enter the price : ")))

    def display_data(self):
        print("ITEM CODE \t PRICE")
        for i in range(5):
            print(self.__item_code[i],"\t\t",self.__price[i])

    def calculate_bill(self, quant):
        total_amount = 0
        for i in range(5):
            total_amount = total_amount+self.__price[i]*quant[i]
        print("*****BILL*****")
        print("ITEM \t PRICE \t QUANTITY \t SUBTOTAL")
        for i in range(5):
            print(self.__item_code[i],"\t",self.__price[i],"\t",quant[i],"\t\t",quant[i]*self.__price[i])
        print("\t\t\t------------------")
        print("\t\t\t Total =", total_amount)
        print("\t\t\t------------------")

s = store()
s.get_data()
s.display_data()
q = []
print("Enter the quantity of each item : ")
for i in range(5):
    q.append(int(input()))
s.calculate_bill(q)
