class Bank:
    def __init__(self,saldo):
        self.__saldo = saldo
  
    # def deposit(self,amount):
    #     self.saldo += amount
        
    #     print(f"Deposit Successful. Your new balance is {self.saldo}")

    def set_saldo(self,money):
        self.__saldo = money

    def get_saldo(self):
        return self.__saldo
    
ucup = Bank(1000)
print(ucup.__dict__)

yudi = Bank(8000)
yudi.set_saldo(90000)
print(yudi.get_saldo())

