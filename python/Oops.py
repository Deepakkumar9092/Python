#Abstraction
#Hiding unecessary data and proving only revelent data is known as Abstraction
class Car:
    def __init__(self):#Constructor
        self.acc = False
        self.brk = False
        self.clutch = False

    def Start(self): #Methods
        self.acc =  True
        self.clutch = True
        print("Car Started...")
    
c1= Car()
c1.Start()

#Create Account class with 2 attributes - dbalance & accNumber. Create methods for debit and creadit & printing the balance
class Account:
    
    def __init__(self, bal, acc):
        self.bal = bal
        self.acc = acc        

    def debit(self, amount):
        self.bal -= amount
        print("Rs",amount,"Balance is Debited")
        print("Total Amount ",self.get_bal())

    def credit(self,amount):
        self.bal +=  amount
        print("Rs",amount,"Balance is Credited")
        print("Total Balance ",self.get_bal())

    def get_bal(self):
        return self.bal

acc1 = Account(9000,42932849343)
acc1.credit(3000)
acc1.debit(5000)
acc1.credit(34535)
acc1.get_bal()



