class  BankCard:
    def __init__(self, account, name, balance):
        self.account = account
        self.name = name
        self.balance = balance

    def save_money(self,money):
        self.balance += money

    def draw_money(self,money):
        if self.balance >= money:
            self.balance -= money
            print("取款金额是{1}, 余额为{0}".format(money, self.balance))
        else:
            print("余额不足")


    def check_balance(self):
        print("账号：{} 名字：{} 余额：{}".format(self.account, self.name, self.balance))

    def transfer(self, card, money):
        if self.balance >= money:
            self.balance -= money
            card.balance += money
            print("成功转账{}".format(money))
        else:
            print("余额不足")

class Atm:
    def __init__(self, card=None):
        self.card = card

    def insert_card(self, card):
        self.card = card

    def save_money(self, money):
        self.card.save_money(money)

    def draw_money(self, money):
        self.card.draw_money(money)

    def check_balance(self):
        self.card.check_balance()

    def transfer(self, card, money):
        self.card.transfer(card, money)

card1 = BankCard("622122", "王皮皮", 10000)
card2 = BankCard("733133", "王彬彬", 20)

atm = Atm()
atm.insert_card(card1)
atm.check_balance()
atm.save_money(80)
atm.check_balance()