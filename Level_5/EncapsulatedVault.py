class Vault:
    def __init__(self, pin, balance):
        self.__pin = pin          # Private attribute
        self.__balance = balance  # Private attribute

    def set_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Access Denied!")

    def check_balance(self, pin):
        if pin == self.__pin:
            print("Balance:", self.__balance)
        else:
            print("Access Denied!")

    def deposit(self, pin, amount):
        if pin == self.__pin:
            self.__balance += amount
            print("Deposit Successful.")
            print("Updated Balance:", self.__balance)
        else:
            print("Access Denied!")


# Driver Code
v = Vault(1234, 5000)

v.check_balance(1234)
v.deposit(1234, 2000)
v.check_balance(1234)

v.deposit(1111, 1000)
v.check_balance(1111)

v.set_pin(1234, 4321)
v.check_balance(4321)