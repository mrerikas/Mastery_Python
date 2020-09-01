class Bankas():
    country = 'Lietuvis'

    def __init__(self, name, account, status):
        self.name = name
        self.account = account
        self.status = status

    def withdraw(self):
        ammount = int(input("Norima suma issimti?: "))
        if ammount > self.account:
            print(f'Jusu saskaitoje neuztenka pinigu')
        else:
            self.account -= ammount
            return f'Jusu saskaitoje dabar liko {self.account}'

    def add_money(self):
        addammount = int(input('Prasau pasirinkti suma kuria norite ideti: '))
        self.account += addammount
        return f'Sekmingai idejote pinigu, dabar jusu saskaitoje yra {self.account} pinigu'

    def check_ammount(self):
        return self.account

    def get_loan(self):
        if self.account >= 10000 and not self.status == 'Blogas':
            self.get_loan = 10000
            print(
                f'Your request accepted. Your account balance is:{self.account} Eur and loan balance is:{self.get_loan} Eur.')
            return f'TOTAL: {self.account + self.get_loan} Eur'
        return f'Your request is declined'

    def loan_balance(self):
        return self.get_loan


p1 = Bankas('Erikas', 10000, 'VIP')
p2 = Bankas('Arturas', 10000, 'VIP')
p3 = Bankas('Sigita', 5000, 'Paprastas')
p4 = Bankas('Andrius', 50, 'Blogas')
