class Account:
    def __init__(self, name, balance):
        self.owner = name
        self.balance = balance
    def deposit(self, sum):
        self.balance +=sum

    def withdraw(self, sum):
        if(sum > self.balance):
            print("You cant afford it")
        else:
            self.balance -= sum


acc1 = Account("Jordan", 1000)

acc1.deposit(1000)
acc1.deposit(1000)
acc1.deposit(1000)
acc1.withdraw(3000)
print(acc1.balance)