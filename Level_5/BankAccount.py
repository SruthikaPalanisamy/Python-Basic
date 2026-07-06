class BankAccount:
    def __init__(self , owner  , balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amt):
        self.balance += amt
        print("balance" , self.balance)
    def withdraw(self , amt):
        if(amt > self.balance):
            return "insufficient"
        else:
            self.balance -= amt
        print("Balance is" , self.balance)
    
    def get_statement(self  ):
        print("The owner name is: " ,  self.owner)
        print(f"The balance amt of { self.owner} is { self.balance}")


bk = BankAccount("Sruthika" )
bk.deposit(500)
bk.withdraw(100)
bk.get_statement()


