class Bank:
    def __init__(self, s):
        self.owner = s
        self.balance = 0
    
    def get(self):
        print(self.owner, "has", self.balance, "money")

    def depos(self, x):
        self.balance += x
    
    def withd(self, x):
        if x <= self.balance:
            self.balance -= x
        else:
            print("Not enough")

x = Bank("Kasym")
x.depos(100)
x.depos(50)
x.get()
x.withd(150)
x.get()
x.withd(10)
x.depos(10)
x.get()