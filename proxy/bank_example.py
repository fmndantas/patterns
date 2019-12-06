from abc import ABCMeta, abstractmethod


# Subject
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_payment(self):
        pass


# Real subject
class Bank(Payment):
    def do_payment(self):
        print("\nBank:: doing payment")


# Proxy
class DebitCard(Payment):
    def __init__(self, bank: Bank):
        self.bank = bank

    def do_payment(self):
        print("\nDebitCard:: do_payment")
        self.bank.do_payment()


class Client:
    def __init__(self, debit_card: DebitCard):
        self.debit_card = debit_card

    def buy_item(self, item):
        print(
            f"""Client:: I\'ll buy a {item}"""
            """\nClient:: But I don\'t have money"""
            """\nClient:: So, I\'ll use my debit card"""
        )

        self.debit_card.do_payment()


if __name__ == '__main__':
    b = Bank()
    dc = DebitCard(b)
    c = Client(dc)
    c.buy_item("Python 3.20b")
