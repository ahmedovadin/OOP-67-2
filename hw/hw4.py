rates = {
   "KGS": 1,
   "USD": 89,
   "EUR": 96,
   "RUB": 1.2
}

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency.strip().upper()

    def convert_to_kgs(self):
        if self.currency == 'KGS':
            return rates[self.currency]
        else:
            return self.amount * rates[self.currency]

    def convert_to_self_currency(self, other):
        if self.currency == other.currency:
            return other.amount
        elif self.currency == 'KGS':
            return other.amount * rates[other.currency]
        else:
            return other.amount / rates[self.currency]

    def __add__(self, other):
        resolved_amount = self.convert_to_self_currency(other)
        return Money(round(self.amount + resolved_amount, 2), self.currency)


    def __sub__(self, other):
        resolved_amount = self.convert_to_self_currency(other)
        return Money(round(self.amount - resolved_amount, 2), self.currency)

    def __mul__(self, number):
        return Money(self.amount * number, self.currency)

    def __truediv__(self, number):
        return Money(self.amount / number, self.currency)

    def __str__(self):
        return str(f'{self.amount} {self.currency}')



money1 = Money(100, 'USD')
money2 = Money(500, 'KGS')

result1 = money1 + money2
result2 = money1 - money2
print(result1)
print(result2)
print(money1 * 2)
print(money1 / 2)
print(f'Money 1: {money1}')
print(f'Money 2: {money2}')