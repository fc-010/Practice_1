class NotEnoughMoneyError(Exception):
    pass


class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def add_money(self, amount):
        self.balance += amount

    def take_money(self, amount):
        if amount > self.balance:
            raise NotEnoughMoneyError(
                f"Cannot withdraw {amount}, balance is {self.balance}"
            )
        self.balance -= amount


person1 = Account(" Tom Holland ", 1000)
person1.add_money(500)
person1.take_money(300)

print(person1.balance)

try:
    person1.take_money(5000)
except NotEnoughMoneyError as e:
    print("Error:", e)