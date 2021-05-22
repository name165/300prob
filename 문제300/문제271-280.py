import random
class account:
    counter = 0
    dep_c = 0
    def __init__(self,name,money,v):
        self.bname = "SC은행"
        self.num = str(random.randint(100,999)) + str(random.randint(10,99)) + str(random.randint(100000,999999))
        self.name = name
        self.money = money
        account.counter = v+1
    def get_account_num(self):
        print(account.counter)
    def deposit(self, money):
        self.money += money
        account.dep_c += 1
        if dep_c == 5:
            money *= 1.01
            dep_c = 0
    def withdraw(self, money):
        self.money -= money
    def display_info(self):
        print(self.bname,self.name,self.num,self.money)

ac = []
ac.append(account("a",150000,0))
ac.append(account("b",1300000,1))
ac.append(account("c",2500000,2))

for i in ac:
    if i.money >= 1000000:
        i.display_info()


