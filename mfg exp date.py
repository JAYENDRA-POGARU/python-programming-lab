import datetime
class product:
    def __init__(self):
        self.manufacture = datetime.datetime.strptime(input("Enter manufacturing date (mm/dd/yyyy): "),'%m/%d/%Y')
        self.expiry = datetime.datetime.strptime(input("Enter expiry date (mm/dd/yyyy): "),'%m/%d/%Y')
    def time_to_expire(self):
        today = datetime.datetime.now()
        if(today > self.expiry):
            print('Product has already expired')
        else:
            time_left = self.expiry.date() - datetime.datetime.now().date()
            print('Time left: ',time_left)
    def show(self):
        print('Expiry: ',self.expiry)
        print('Manufacturing: ',self.manufacture)
x=product()
x.time_to_expire()
