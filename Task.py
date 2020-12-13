import uuid
from datetime import datetime


class My_bank_account:
    bank_fee = 0.01

    def __init__(self, name):
        self.name = name
        self.account_id = uuid.uuid4()
        self.balance = 0.0
        self.transactions = []

    def input_cash(self, amount):
        self.balance += amount - (amount * self.bank_fee)
        self.transactions.append((amount, 'Пополнение', datetime.now().strftime('%d-%m-%Y')))

    def output_cash(self, amount):
        if self.balance >= amount:
            self.balance -= amount + (amount * self.bank_fee)
            self.transactions.append((amount, 'Снятие наличных', datetime.now().strftime('%d-%m-%Y')))
        else:
            print('Недостаточно средств, Бро')

    def get_balance(self):
        return self.balance



my_bill = My_bank_account('Мой счёт')
my_bill.input_cash(500)
print('Ваш счёт пополнен на ' + str(my_bill.get_balance()) + " \nСпасибо, что выбрали наш банк)")
my_bill.output_cash(200)
print('Средства выведены. Текущий остаток - ' + str(my_bill.get_balance()))
my_bill.output_cash(100)
print('Средства выведены. Текущий остаток - ' + str(my_bill.get_balance()))
print('Текущий баланс - ' + str(my_bill.get_balance()))
print(my_bill.transactions)
