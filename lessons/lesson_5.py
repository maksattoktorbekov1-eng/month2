class Money:

    def __init__(self, amount=0):
        self.amount = amount

    def __str__(self):
        return f"Money obj amount {self.amount}"

    def __eq__(self, other):
        if self.amount == other.amount:
            return True
        return False

    def __gt__(self, other):
        if self.amount >= other.amount:
            return True
        return False

    def __add__(self, other):
        new_money = Money(amount=self.amount + other.amount)
        return new_money

    # subtraction
    def __sub__(self, other):
        new_money = Money(amount=self.amount - other.amount)


# le - less  or eqeal:
# lt - less then:<
# gt - greater then:>,<
# ge - great then or equal:>=,<=
money_you = Money(amount=10000)
money_my = Money(amount=1000)
print(money_my)
print(money_you)

print(money_you > money_my)
print(money_my < money_you)
print(money_my == money_you)
print(f" Add two money objects  Money Obj amount")
